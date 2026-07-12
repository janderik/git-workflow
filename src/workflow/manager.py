"""Git workflow manager."""

import subprocess
import os
from typing import Optional, List
from pathlib import Path


class WorkflowManager:
    """
    Manage Git workflows and automation.
    
    Supports GitFlow, GitHub Flow, and custom workflows.
    """
    
    def __init__(self, repo_path: Optional[str] = None):
        """Initialize the workflow manager."""
        self.repo_path = Path(repo_path) if repo_path else Path.cwd()
    
    def _run_git(self, *args) -> str:
        """Run a git command."""
        result = subprocess.run(
            ['git'] + list(args),
            cwd=self.repo_path,
            capture_output=True,
            text=True
        )
        return result.stdout
    
    def init_workflow(self, workflow_type: str = "gitflow"):
        """Initialize a workflow in the repository."""
        if workflow_type == "gitflow":
            self._init_gitflow()
        elif workflow_type == "github":
            self._init_github_flow()
    
    def _init_gitflow(self):
        """Initialize GitFlow workflow."""
        # Create main branches if they don't exist
        branches = self._run_git('branch').splitlines()
        
        if 'main' not in branches and 'master' not in branches:
            self._run_git('checkout', '-b', 'main')
        
        if 'develop' not in branches:
            self._run_git('checkout', '-b', 'develop')
            self._run_git('checkout', 'main')
    
    def _init_github_flow(self):
        """Initialize GitHub Flow workflow."""
        branches = self._run_git('branch').splitlines()
        
        if 'main' not in branches and 'master' not in branches:
            self._run_git('checkout', '-b', 'main')
    
    def start_feature(self, name: str):
        """Start a new feature branch."""
        self._run_git('checkout', 'develop')
        self._run_git('checkout', '-b', f'feature/{name}')
    
    def finish_feature(self, name: str):
        """Finish a feature branch."""
        self._run_git('checkout', 'develop')
        self._run_git('merge', f'feature/{name}')
        self._run_git('branch', '-d', f'feature/{name}')
    
    def start_release(self, version: str):
        """Start a release branch."""
        self._run_git('checkout', 'develop')
        self._run_git('checkout', '-b', f'release/{version}')
    
    def finish_release(self, version: str):
        """Finish a release branch."""
        self._run_git('checkout', 'main')
        self._run_git('merge', f'release/{version}')
        self._run_git('tag', f'v{version}')
        self._run_git('checkout', 'develop')
        self._run_git('merge', f'release/{version}')
        self._run_git('branch', '-d', f'release/{version}')
    
    def get_current_branch(self) -> str:
        """Get the current branch name."""
        return self._run_git('rev-parse', '--abbrev-ref', 'HEAD').strip()
    
    def get_branches(self) -> List[str]:
        """Get list of all branches."""
        return self._run_git('branch').splitlines()
