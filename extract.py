import zipfile
import os
from pathlib import Path

try:
    # Find the zip file
    possible_paths = [
        'escortwp.zip',
        '/home/user/escortwp.zip',
        '/vercel/share/v0-project/escortwp.zip',
        Path.cwd() / 'escortwp.zip'
    ]
    
    zip_path = None
    for path in possible_paths:
        if os.path.exists(path):
            zip_path = path
            print(f'[v0] Found zip at: {zip_path}')
            break
    
    if not zip_path:
        print('[v0] Zip file not found')
        print('[v0] Current directory:', os.getcwd())
        print('[v0] Files:', os.listdir('.'))
    else:
        extract_dir = '/vercel/share/v0-project'
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        print('[v0] Extraction complete')
except Exception as e:
    print(f'[v0] Error: {str(e)}')
