#!/usr/bin/env python3
"""
Convert Jupyter notebooks to HTML for GitHub Pages hosting.

This script:
1. Finds all .ipynb files in the repository
2. Converts them to HTML using nbconvert
3. Maintains the same directory structure
4. Generates an index of converted notebooks
5. Provides options for custom styling
"""

import os
import sys
import subprocess
from pathlib import Path
import json
from datetime import datetime

def find_notebooks(root_dir="."):
    """Find all Jupyter notebook files in the directory tree."""
    root_path = Path(root_dir)
    notebooks = []
    
    for notebook_path in root_path.rglob("*.ipynb"):
        # Skip checkpoint files
        if ".ipynb_checkpoints" not in str(notebook_path):
            notebooks.append(notebook_path)
    
    return sorted(notebooks)

def convert_notebook_to_html(notebook_path, output_dir="html_notebooks"):
    """Convert a single notebook to HTML."""
    try:
        # Create output directory structure
        relative_path = notebook_path.relative_to(".")
        html_path = Path(output_dir) / relative_path.with_suffix(".html")
        html_path.parent.mkdir(parents=True, exist_ok=True)
          # Convert using nbconvert (using python -m for Windows compatibility)
        cmd = [
            "python", "-m", "nbconvert",
            "--to", "html",
            "--output", str(html_path.absolute()),
            str(notebook_path)
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Converted: {notebook_path} -> {html_path}")
            return html_path
        else:
            print(f"❌ Failed to convert {notebook_path}")
            print(f"Error: {result.stderr}")
            return None
            
    except Exception as e:
        print(f"❌ Error converting {notebook_path}: {e}")
        return None

def get_notebook_description(notebook_path):
    """Extract a brief description from notebook content."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb_data = json.load(f)
            
        # Try to get description from first few markdown cells
        cells = nb_data.get('cells', [])
        description = ""
        
        for cell in cells[:3]:  # Check first 3 cells
            if cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', []))
                # Skip title lines and get content
                lines = source.split('\n')
                for line in lines:
                    line = line.strip()
                    if line and not line.startswith('#') and len(line) > 20:
                        description = line[:150] + "..." if len(line) > 150 else line
                        break
                if description:
                    break
        
        if not description:
            # Fallback based on notebook path/name
            path_parts = str(notebook_path).lower()
            if 'machine-learning' in path_parts or 'ml' in path_parts:
                description = "Machine learning analysis and model development"
            elif 'visualization' in path_parts or 'viz' in path_parts:
                description = "Data visualization and exploratory analysis"
            elif 'nlp' in path_parts:
                description = "Natural language processing and text analysis"
            elif 'sql' in path_parts:
                description = "SQL database analysis and queries"
            elif 'python' in path_parts:
                description = "Python programming fundamentals and applications"
            else:
                description = "Data analysis and exploration"
        
        return description
        
    except Exception as e:
        return "Data analysis and exploration"

def get_notebook_title(notebook_path):
    """Extract title from notebook metadata or filename."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb_data = json.load(f)
            
        # Try to get title from metadata
        metadata = nb_data.get('metadata', {})
        title = metadata.get('title', '')
        
        if not title:
            # Try to get from first markdown cell
            cells = nb_data.get('cells', [])
            for cell in cells:
                if cell.get('cell_type') == 'markdown':
                    source = ''.join(cell.get('source', []))
                    if source.startswith('#'):
                        title = source.split('\n')[0].lstrip('#').strip()
                        break
        
        if not title:
            # Use filename as fallback
            title = notebook_path.stem.replace('-', ' ').replace('_', ' ').title()
            
        return title
        
    except Exception as e:
        print(f"Warning: Could not extract title from {notebook_path}: {e}")
        return notebook_path.stem.replace('-', ' ').replace('_', ' ').title()

def generate_html_index(converted_notebooks, output_file="notebook_index.html"):
    """Generate an HTML index of all converted notebooks with Tailwind CSS and featured projects."""
    
    # Group notebooks by directory
    notebooks_by_dir = {}
    for notebook_path, html_path in converted_notebooks:
        dir_name = str(notebook_path.parent)
        if dir_name == ".":
            dir_name = "Root"
        
        if dir_name not in notebooks_by_dir:
            notebooks_by_dir[dir_name] = []
        
        title = get_notebook_title(notebook_path)
        notebooks_by_dir[dir_name].append({
            'title': title,
            'notebook_path': notebook_path,
            'html_path': html_path,
            'html_url': str(html_path).replace('\\', '/'),
            'description': get_notebook_description(notebook_path)
        })
    
    # Define featured projects
    featured_projects = [
        {
            'title': 'SpaceX Launch Prediction',
            'description': 'Machine learning model to predict SpaceX Falcon 9 first stage landing success',
            'path': 'html_notebooks/Capstone_Data_Science_SpaceY/spacex-machine-learning-prediction.html',
            'tags': ['Machine Learning', 'Classification', 'Data Science'],
            'icon': '🚀'
        },
        {
            'title': 'Car Price Prediction Model',
            'description': 'End-to-end data science project for automobile price prediction',
            'path': 'html_notebooks/Data_Analysis/car-price-model-development.html',
            'tags': ['Regression', 'EDA', 'Model Development'],
            'icon': '🚗'
        },
        {
            'title': 'Sentiment Analysis NLP',
            'description': 'Natural language processing for sentiment classification',
            'path': 'html_notebooks/NLP/09_Advanced_Projects/01_sentiment_classification_project.html',
            'tags': ['NLP', 'Deep Learning', 'Text Analysis'],
            'icon': '💬'
        },
        {
            'title': 'Interactive Data Visualization',
            'description': 'Advanced plotly dashboards and interactive visualizations',
            'path': 'html_notebooks/Visualization/Interactive-Data-Visualization-with-Plotly.html',
            'tags': ['Visualization', 'Plotly', 'Interactive'],
            'icon': '📊'
        }
    ]
    
    # Generate HTML with Tailwind CSS
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Analytics Python - Portfolio</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        'github': '#24292e',
                        'jupyter': '#f37626'
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="bg-gray-50 min-h-screen">
    <!-- Header -->
    <header class="bg-white shadow-sm border-b border-gray-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
            <div class="text-center">
                <h1 class="text-4xl font-bold text-gray-900 mb-2">
                    📊 Data Analytics Python Portfolio
                </h1>
                <p class="text-lg text-gray-600 mb-2">
                    Comprehensive collection of data science, machine learning, and analytics projects
                </p>
                <p class="text-sm text-gray-500">
                    Generated on {datetime.now().strftime('%B %d, %Y')} • {len(converted_notebooks)} Total Projects
                </p>
            </div>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <!-- Featured Projects -->
        <section class="mb-12">
            <div class="flex items-center justify-between mb-6">
                <h2 class="text-2xl font-bold text-gray-900">🌟 Featured Projects</h2>
                <span class="text-sm text-gray-500">Handpicked highlights</span>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">"""
    
    for project in featured_projects:
        html_content += f"""
                <div class="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 overflow-hidden group">
                    <div class="p-6">
                        <div class="flex items-start justify-between mb-3">
                            <span class="text-3xl">{project['icon']}</span>
                            <span class="bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded-full">Featured</span>
                        </div>
                        <h3 class="font-semibold text-gray-900 mb-2 group-hover:text-blue-600 transition-colors">
                            <a href="{project['path']}" class="stretched-link">{project['title']}</a>
                        </h3>
                        <p class="text-gray-600 text-sm mb-3 line-clamp-2">{project['description']}</p>
                        <div class="flex flex-wrap gap-1">
                            {''.join([f'<span class="bg-gray-100 text-gray-700 text-xs px-2 py-1 rounded">{tag}</span>' for tag in project['tags']])}
                        </div>
                    </div>
                </div>"""
    
    html_content += """
            </div>
        </section>

        <!-- All Projects by Category -->
        <section>
            <div class="flex items-center justify-between mb-6">
                <h2 class="text-2xl font-bold text-gray-900">📁 All Projects by Category</h2>
                <span class="text-sm text-gray-500">Organized by domain</span>
            </div>
"""    
    total_notebooks = sum(len(notebooks) for notebooks in notebooks_by_dir.values())
    
    # Directory icons and descriptions
    dir_info = {
        'Capstone_Data_Science_SpaceY': {'icon': '🚀', 'name': 'SpaceX Capstone', 'desc': 'End-to-end data science project'},
        'Capstone_StackOverflow_Survey': {'icon': '📋', 'name': 'StackOverflow Survey', 'desc': 'Developer survey analysis'},
        'Data_Analysis': {'icon': '📈', 'name': 'Data Analysis', 'desc': 'Core data analysis projects'},
        'ML': {'icon': '🤖', 'name': 'Machine Learning', 'desc': 'Classification, regression, and clustering'},
        'NLP': {'icon': '💬', 'name': 'Natural Language Processing', 'desc': 'Text analysis and language models'},
        'Python': {'icon': '🐍', 'name': 'Python Fundamentals', 'desc': 'Core Python programming concepts'},
        'SQL': {'icon': '🗄️', 'name': 'SQL & Databases', 'desc': 'Database analysis and queries'},
        'Visualization': {'icon': '📊', 'name': 'Data Visualization', 'desc': 'Charts, dashboards, and interactive plots'},
        'Root': {'icon': '📁', 'name': 'General Projects', 'desc': 'Miscellaneous notebooks'}
    }
    
    for dir_name, notebooks in sorted(notebooks_by_dir.items()):
        info = dir_info.get(dir_name, {'icon': '📁', 'name': dir_name, 'desc': 'Project collection'})
        
        html_content += f"""
            <div class="mb-8 bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
                <div class="bg-gradient-to-r from-blue-50 to-indigo-50 px-6 py-4 border-b border-gray-200">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-3">
                            <span class="text-2xl">{info['icon']}</span>
                            <div>
                                <h3 class="text-lg font-semibold text-gray-900">{info['name']}</h3>
                                <p class="text-sm text-gray-600">{info['desc']}</p>
                            </div>
                        </div>
                        <span class="bg-blue-100 text-blue-800 text-sm font-medium px-3 py-1 rounded-full">
                            {len(notebooks)} projects
                        </span>
                    </div>
                </div>
                
                <div class="p-6">
                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">"""
        
        for notebook in sorted(notebooks, key=lambda x: x['title']):
            html_content += f"""
                        <div class="group relative bg-gray-50 rounded-lg p-4 hover:bg-blue-50 transition-colors duration-200 border border-gray-100 hover:border-blue-200">
                            <div class="flex items-start justify-between mb-2">
                                <h4 class="font-medium text-gray-900 group-hover:text-blue-700 transition-colors text-sm leading-tight">
                                    <a href="{notebook['html_url']}" class="stretched-link">{notebook['title']}</a>
                                </h4>
                                <svg class="w-4 h-4 text-gray-400 group-hover:text-blue-500 transition-colors flex-shrink-0 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path>
                                </svg>
                            </div>
                            <p class="text-xs text-gray-600 mb-2 line-clamp-2">{notebook['description']}</p>
                            <div class="flex items-center justify-between text-xs">
                                <span class="text-gray-500 font-mono">{notebook['notebook_path'].name}</span>
                                <a href="{notebook['notebook_path']}" class="text-blue-600 hover:text-blue-800 transition-colors">
                                    � Download
                                </a>
                            </div>
                        </div>"""
        
        html_content += """
                    </div>
                </div>
            </div>"""
    
    html_content += f"""
        </section>
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-gray-200 mt-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <div class="text-center">
                <div class="flex items-center justify-center space-x-6 mb-4">
                    <div class="flex items-center space-x-2">
                        <span class="text-lg">📊</span>
                        <span class="text-sm font-medium text-gray-900">{total_notebooks} Total Projects</span>
                    </div>
                    <div class="flex items-center space-x-2">
                        <span class="text-lg">🗂️</span>
                        <span class="text-sm font-medium text-gray-900">{len(notebooks_by_dir)} Categories</span>
                    </div>
                    <div class="flex items-center space-x-2">
                        <span class="text-lg">⭐</span>
                        <span class="text-sm font-medium text-gray-900">{len(featured_projects)} Featured</span>
                    </div>
                </div>
                <p class="text-sm text-gray-500">
                    Last updated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
                </p>
                <div class="mt-4">
                    <a href="index.html" class="inline-flex items-center px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition-colors">
                        ← Back to Main Portfolio
                    </a>
                </div>
            </div>
        </div>
    </footer>

    <style>
        .stretched-link::after {{
            position: absolute;
            top: 0;
            right: 0;
            bottom: 0;
            left: 0;
            z-index: 1;
            content: "";
        }}
        
        .line-clamp-2 {{
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
    </style>
</body>
</html>
"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"📄 Generated modern Tailwind index: {output_file}")

def main():
    """Main conversion process."""
    print("🔍 Finding Jupyter notebooks...")
    notebooks = find_notebooks()
    
    if not notebooks:
        print("❌ No Jupyter notebooks found!")
        return
    
    print(f"📊 Found {len(notebooks)} notebooks")
      # Check if nbconvert is available
    try:
        subprocess.run(["python", "-m", "nbconvert", "--version"], 
                      capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ nbconvert not found! Please install it:")
        print("   pip install nbconvert")
        return
    
    # Convert notebooks
    print("\n🔄 Converting notebooks to HTML...")
    converted_notebooks = []
    failed_conversions = []
    
    for notebook_path in notebooks:
        html_path = convert_notebook_to_html(notebook_path)
        if html_path:
            converted_notebooks.append((notebook_path, html_path))
        else:
            failed_conversions.append(notebook_path)
    
    # Generate index
    if converted_notebooks:
        print(f"\n📝 Generating HTML index...")
        generate_html_index(converted_notebooks)
    
    # Summary
    print(f"\n✅ Conversion complete!")
    print(f"   - Converted: {len(converted_notebooks)} notebooks")
    print(f"   - Failed: {len(failed_conversions)} notebooks")
    
    if failed_conversions:
        print("\n❌ Failed conversions:")
        for notebook in failed_conversions:
            print(f"   - {notebook}")
    
    print(f"\n📁 HTML files are in: html_notebooks/")
    print(f"📄 Index file: notebook_index.html")

if __name__ == "__main__":
    main()
