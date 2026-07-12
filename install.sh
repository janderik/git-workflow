#!/bin/bash
# Git Workflow Installation Script

echo "Installing Git Workflow..."

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not installed."
    exit 1
fi

# Install Python dependencies
pip install -r requirements.txt

# Make CLI executable
chmod +x cli.py

# Create symlink for global access (optional)
if [ "$1" = "--global" ]; then
    ln -sf "$(pwd)/cli.py" /usr/local/bin/git-workflow
    echo "Installed globally as 'git-workflow'"
fi

echo "Installation complete!"
echo "Run 'python cli.py --help' to get started."
