import zipfile
import os
from pathlib import Path

try:
    # Get the current working directory and find the zip
    cwd = os.getcwd()
    print(f'[v0] Current directory: {cwd}')
    print(f'[v0] Files in cwd: {os.listdir(cwd)}')
    
    zip_path = os.path.join(cwd, 'escortwp.zip')
    extract_dir = cwd
    
    if os.path.exists(zip_path):
        print(f'[v0] Found zip at: {zip_path}')
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        print('[v0] Extraction complete')
        # List extracted files
        extracted_items = os.listdir(extract_dir)
        print('[v0] Extracted items count:', len(extracted_items))
        print('[v0] First items:', extracted_items[:5])
    else:
        print('[v0] Zip file not found at:', zip_path)
except Exception as e:
    print(f'[v0] Error: {str(e)}')
