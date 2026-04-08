import os
import subprocess

# Check current directory
print(f'[v0] Current working directory: {os.getcwd()}')

# List files in /vercel/share/v0-project
project_dir = '/vercel/share/v0-project'
if os.path.exists(project_dir):
    print(f'[v0] Files in {project_dir}:')
    try:
        items = os.listdir(project_dir)
        for item in sorted(items):
            full_path = os.path.join(project_dir, item)
            is_dir = os.path.isdir(full_path)
            size = os.path.getsize(full_path) if os.path.isfile(full_path) else 'DIR'
            print(f'  {item} - {size}')
    except Exception as e:
        print(f'[v0] Error listing: {e}')
else:
    print(f'[v0] Directory does not exist: {project_dir}')

# Try to find escortwp.zip anywhere
print('\n[v0] Searching for escortwp.zip...')
try:
    result = subprocess.run(['find', '/', '-name', 'escortwp.zip', '-type', 'f'], 
                          capture_output=True, text=True, timeout=5)
    if result.stdout:
        print('[v0] Found:', result.stdout)
    else:
        print('[v0] Not found in system')
except Exception as e:
    print(f'[v0] Error searching: {e}')
