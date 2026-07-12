# Git Workflow

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A git workflow automation tool with custom hooks, templates, and commands. Streamline your development workflow with consistent practices.

## Features

- **Workflow templates** - Pre-configured GitFlow, GitHub Flow, etc.
- **Custom hooks** - Pre-commit, post-commit, pre-push hooks
- **Git commands** - Extended git commands for common tasks
- **Branch management** - Automated branch creation and cleanup
- **Release automation** - Streamlined release process

## Installation

```bash
git clone https://github.com/janderik/git-workflow.git
cd git-workflow
chmod +x install.sh
./install.sh
```

## Usage

```bash
# Initialize workflow in a repo
git workflow init

# Create feature branch
git workflow feature start my-feature

# Create release
git workflow release start 1.0.0

# Run hooks manually
git workflow hooks run pre-commit
```

## Contributing

Contributions are welcome!

## License

MIT License
