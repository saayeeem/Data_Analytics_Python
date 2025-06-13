#!/usr/bin/env python3
"""
Script to fix widget metadata issues in Jupyter notebooks that cause nbconvert errors.
Removes the problematic "widgets" metadata section from notebooks.
"""

import os
import json
import sys
from pathlib import Path

def fix_notebook_widgets(notebook_path):
    """Fix widgets metadata in a single notebook file."""
    try:
        # Read the notebook
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Check if widgets metadata exists
        if 'metadata' in notebook and 'widgets' in notebook['metadata']:
            print(f"Fixing widgets metadata in: {notebook_path}")
            
            # Remove the widgets metadata
            del notebook['metadata']['widgets']
            
            # Write the fixed notebook back
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(notebook, f, indent=1, ensure_ascii=False)
            
            return True
        else:
            print(f"No widgets metadata found in: {notebook_path}")
            return False
            
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in {notebook_path}: {e}")
        return False
    except Exception as e:
        print(f"ERROR: Failed to process {notebook_path}: {e}")
        return False

def main():
    """Main function to fix all notebooks in the workspace."""
    workspace_path = Path('.')
    
    # Find all .ipynb files
    notebook_files = list(workspace_path.rglob('*.ipynb'))
    
    print(f"Found {len(notebook_files)} notebook files")
    
    fixed_count = 0
    
    for notebook_path in notebook_files:
        # Skip checkpoint files
        if '.ipynb_checkpoints' in str(notebook_path):
            continue
            
        if fix_notebook_widgets(notebook_path):
            fixed_count += 1
    
    print(f"\nFixed {fixed_count} notebooks")
    
    # Test a few notebooks to make sure they can be converted
    test_notebooks = [
        'Visualization/Matplotlib-Line-Plots-and-Canadian-Immigration-Exploration.ipynb',
        'Visualization/Pie-Charts-Box-Plots-Scatter-Plots-and-Bubble-Plots-py-v2.0.ipynb',
        'SQL/Sayem_SQL_Querying.ipynb'
    ]
    
    print("\nTesting notebook conversion for a few fixed notebooks:")
    for notebook in test_notebooks:
        if os.path.exists(notebook):
            try:
                # Test JSON validity
                with open(notebook, 'r') as f:
                    json.load(f)
                print(f"✓ {notebook} - JSON is valid")
            except Exception as e:
                print(f"✗ {notebook} - JSON error: {e}")

if __name__ == "__main__":
    main()
