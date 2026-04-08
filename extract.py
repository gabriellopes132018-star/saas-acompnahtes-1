import zipfile
import os
from pathlib import Path

try:
    # Fixed path for the zip file
    zip_path = '/vercel/share/v0-project/escortwp.zip'
    extract_dir = '/vercel/share/v0-project'
    
    print(f'[v0] Extracting from: {zip_path}')
    
    if os.path.exists(zip_path):
        print(f'[v0] Found zip at: {zip_path}')
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        print('[v0] Extraction complete')
        # List extracted files
        extracted_items = os.listdir(extract_dir)
        print('[v0] Extracted items count:', len(extracted_items))
        print('[v0] Main dirs/files:', [item for item in extracted_items if not item.startswith('.')])
    else:
        print('[v0] Zip file not found at:', zip_path)
except Exception as e:
    print(f'[v0] Error: {str(e)}')
