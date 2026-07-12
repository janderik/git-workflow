#!/usr/bin/env python3
"""
Git Workflow CLI.

A command-line tool for git workflow automation.
"""

import argparse
import sys

from src.workflow.manager import WorkflowManager
from src.hooks.manager import HookManager


def init_command(args):
    """Execute the init command."""
    manager = WorkflowManager()
    manager.init_workflow(args.type)
    print(f"[+] Initialized {args.type} workflow")


def feature_command(args):
    """Execute the feature command."""
    manager = WorkflowManager()
    
    if args.action == 'start':
        manager.start_feature(args.name)
        print(f"[+] Started feature: {args.name}")
    elif args.action == 'finish':
        manager.finish_feature(args.name)
        print(f"[+] Finished feature: {args.name}")


def hooks_command(args):
    """Execute the hooks command."""
    manager = HookManager()
    
    if args.action == 'install':
        manager.install_hooks()
        print("[+] Hooks installed")
    elif args.action == 'remove':
        manager.remove_hooks()
        print("[+] Hooks removed")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Git Workflow Automation"
    )
    
    subparsers = parser.add_subparsers(dest='command')
    
    # Init command
    init_parser = subparsers.add_parser('init', help='Initialize workflow')
    init_parser.add_argument('--type', default='gitflow', choices=['gitflow', 'github'])
    init_parser.set_defaults(func=init_command)
    
    # Feature command
    feature_parser = subparsers.add_parser('feature', help='Feature management')
    feature_parser.add_argument('action', choices=['start', 'finish'])
    feature_parser.add_argument('name', help='Feature name')
    feature_parser.set_defaults(func=feature_command)
    
    # Hooks command
    hooks_parser = subparsers.add_parser('hooks', help='Hook management')
    hooks_parser.add_argument('action', choices=['install', 'remove'])
    hooks_parser.set_defaults(func=hooks_command)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    args.func(args)


if __name__ == '__main__':
    main()
