"""Git hooks manager."""

import os
import stat
from pathlib import Path
from typing import Optional


class HookManager:
    """Manage Git hooks."""
    
    HOOKS_DIR = '.git/hooks'
    
    PRE_COMMIT = """#!/bin/bash
echo "Running pre-commit checks..."
# Add your checks here
"""
    
    POST_COMMIT = """#!/bin/bash
echo "Commit completed successfully!"
"""
    
    PRE_PUSH = """#!/bin/bash
echo "Running pre-push checks..."
# Add your checks here
"""
    
    def __init__(self, repo_path: Optional[str] = None):
        """Initialize the hook manager."""
        self.repo_path = Path(repo_path) if repo_path else Path.cwd()
        self.hooks_dir = self.repo_path / self.HOOKS_DIR
    
    def install_hooks(self):
        """Install default Git hooks."""
        self.hooks_dir.mkdir(parents=True, exist_ok=True)
        
        hooks = {
            'pre-commit': self.PRE_COMMIT,
            'post-commit': self.POST_COMMIT,
            'pre-push': self.PRE_PUSH,
        }
        
        for name, content in hooks.items():
            self._create_hook(name, content)
    
    def _create_hook(self, name: str, content: str):
        """Create a hook file."""
        hook_path = self.hooks_dir / name
        hook_path.write_text(content)
        
        # Make executable
        hook_path.chmod(hook_path.stat().st_mode | stat.S_IEXEC)
    
    def remove_hooks(self):
        """Remove installed hooks."""
        for hook in ['pre-commit', 'post-commit', 'pre-push']:
            hook_path = self.hooks_dir / hook
            if hook_path.exists():
                hook_path.unlink()
