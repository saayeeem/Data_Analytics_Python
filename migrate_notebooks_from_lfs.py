#!/usr/bin/env python3
"""
Script to migrate Jupyter notebooks from Git LFS back to regular Git tracking.
This fixes the issue where GitHub Pages shows LFS pointer content instead of notebook content.
"""

import subprocess
import sys
from pathlib import Path

def run_command(cmd, description):
    """Run a shell command and handle errors."""
    print(f"\n{description}...")
    print(f"Running: {cmd}")
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd='.')
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            return False
        else:
            print(f"Success: {result.stdout}")
            return True
    except Exception as e:
        print(f"Exception: {e}")
        return False

def main():
    """Main function to migrate notebooks from LFS to regular Git."""
    
    print("🔧 Migrating Jupyter notebooks from Git LFS to regular Git tracking")
    print("This will fix GitHub Pages display issues with .ipynb files")
    
    # Step 1: Check if git lfs is available
    if not run_command("git lfs version", "Checking Git LFS availability"):
        print("❌ Git LFS is not available. Please install it first.")
        return False
    
    # Step 2: Find all ipynb files currently in LFS
    print("\n📋 Finding .ipynb files currently tracked by LFS...")
    result = subprocess.run("git lfs ls-files", shell=True, capture_output=True, text=True)
    lfs_files = result.stdout.strip().split('\n') if result.stdout.strip() else []
    ipynb_lfs_files = [f for f in lfs_files if f.endswith('.ipynb')]
    
    if not ipynb_lfs_files:
        print("ℹ️  No .ipynb files found in LFS tracking")
    else:
        print(f"📁 Found {len(ipynb_lfs_files)} .ipynb files in LFS:")
        for f in ipynb_lfs_files[:5]:  # Show first 5
            print(f"   - {f}")
        if len(ipynb_lfs_files) > 5:
            print(f"   ... and {len(ipynb_lfs_files) - 5} more")
    
    # Step 3: Remove .ipynb from LFS tracking (already done by editing .gitattributes)
    print("\n✅ .gitattributes already updated to remove .ipynb from LFS tracking")
    
    # Step 4: Untrack and re-add ipynb files
    print("\n🔄 Migrating .ipynb files from LFS to regular Git...")
    
    # Find all ipynb files in the repository
    ipynb_files = list(Path('.').rglob('*.ipynb'))
    
    if not ipynb_files:
        print("ℹ️  No .ipynb files found in repository")
        return True
    
    print(f"📁 Found {len(ipynb_files)} .ipynb files to migrate")
    
    # Remove files from LFS tracking and Git index
    if not run_command("git rm --cached *.ipynb", "Removing .ipynb files from Git index"):
        # Try alternative approach for recursive removal
        for ipynb_file in ipynb_files:
            run_command(f'git rm --cached "{ipynb_file}"', f"Removing {ipynb_file} from Git index")
    
    # Add files back as regular Git files
    if not run_command("git add *.ipynb", "Adding .ipynb files back as regular Git files"):
        # Try alternative approach for recursive addition
        for ipynb_file in ipynb_files:
            run_command(f'git add "{ipynb_file}"', f"Adding {ipynb_file} as regular Git file")
    
    # Step 5: Show status
    run_command("git status", "Checking Git status after migration")
    
    print("\n🎉 Migration complete!")
    print("\n📝 Next steps:")
    print("1. Review the changes with: git status")
    print("2. Commit the changes with: git commit -m 'fix: Migrate .ipynb files from LFS to regular Git tracking'")
    print("3. Push the changes with: git push origin master")
    print("4. GitHub Pages should now display notebook content properly")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
