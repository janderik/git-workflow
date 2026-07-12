"""Extended git commands."""

import subprocess
from typing import List, Optional


class ExtendedCommands:
    """Extended git commands for workflow automation."""
    
    def __init__(self, repo_path: Optional[str] = None):
        """Initialize extended commands."""
        self.repo_path = repo_path
    
    def _run(self, *args) -> str:
        """Run a git command."""
        result = subprocess.run(
            ['git'] + list(args),
            cwd=self.repo_path,
            capture_output=True,
            text=True
        )
        return result.stdout
    
    def smart_merge(self, branch: str, strategy: str = "recursive") -> str:
        """Smart merge with conflict resolution."""
        return self._run('merge', '-s', strategy, branch)
    
    def interactive_rebase(self, commit_count: int) -> str:
        """Start interactive rebase."""
        return self._run('rebase', '-i', f'HEAD~{commit_count}')
    
    def squash_last(self, count: int, message: str) -> str:
        """Squash last N commits."""
        self._run('reset', f'--soft', f'HEAD~{count}')
        self._run('commit', '-m', message)
        return "Squashed commits"
    
    def changelog(self, from_tag: Optional[str] = None) -> str:
        """Generate changelog from git log."""
        if from_tag:
            return self._run('log', f'{from_tag}..HEAD', '--oneline')
        return self._run('log', '--oneline', '-20')
    
    def cleanup_merged(self) -> str:
        """Delete merged branches."""
        merged = self._run('branch', '--merged').splitlines()
        deleted = []
        
        for branch in merged:
            branch = branch.strip()
            if branch and branch not in ('main', 'master', 'develop'):
                self._run('branch', '-d', branch)
                deleted.append(branch)
        
        return f"Deleted {len(deleted)} branches"
