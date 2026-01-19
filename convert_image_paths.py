#!/usr/bin/env python3
"""
Convert relative image paths to absolute paths in machine-learning-foundations subdirectories.

Changes:
- ../attachments/ → /machine-learning-foundations/attachments/
"""

import os
import re
from pathlib import Path

# Base directory for machine-learning-foundations
BASE_DIR = Path("content/machine-learning-foundations")

# Pattern to match relative image references
# Matches: ![](../attachments/filename.png) or ![alt](../attachments/filename.png)
PATTERN = r'!\[(.*?)\]\(\.\./attachments/([^)]+)\)'

# Replacement pattern
REPLACEMENT = r'![\1](/machine-learning-foundations/attachments/\2)'

def should_process_file(filepath):
    """Check if file should be processed (in subdirectory, not root)."""
    relative_path = filepath.relative_to(BASE_DIR)
    # Only process files in subdirectories (not root level)
    return len(relative_path.parts) > 1

def process_file(filepath):
    """Process a single markdown file and convert paths."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Replace relative paths with absolute paths
        content = re.sub(PATTERN, REPLACEMENT, content)

        # Check if any changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Main function to process all markdown files."""
    print("Converting relative image paths to absolute paths...")
    print(f"Base directory: {BASE_DIR.absolute()}")
    print()

    # Find all markdown files
    md_files = list(BASE_DIR.rglob("*.md"))

    # Filter out _index files and root-level files
    subdirectory_files = [f for f in md_files if should_process_file(f)]

    print(f"Found {len(subdirectory_files)} markdown files in subdirectories")

    if not subdirectory_files:
        print("No files to process!")
        return

    # Process each file
    changes_made = 0
    for filepath in subdirectory_files:
        if process_file(filepath):
            relative_path = filepath.relative_to(BASE_DIR)
            print(f"  ✓ Updated: {relative_path}")
            changes_made += 1

    print()
    print(f"Complete! Updated {changes_made} file(s)")

if __name__ == "__main__":
    main()