import zipfile
import os
from pathlib import Path

try:
    # Verify zip file exists
    import glob
    zip_files = glob.glob('/vercel/share/v0-project/*.zip')
    print(f'[v0] Found zip files: {zip_files}')
    
    if zip_files:
        zip_path = zip_files[0]
        extract_dir = '/vercel/share/v0-project'
        
        print(f'[v0] Extracting from: {zip_path}')
        print(f'[v0] Extracting to: {extract_dir}')
        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        print('[v0] Extraction complete')
        
        # List extracted files
        extracted_items = os.listdir(extract_dir)
        print('[v0] Total items:', len(extracted_items))
        print('[v0] Main dirs/files:', sorted([item for item in extracted_items if not item.startswith('.')]))
    else:
        print('[v0] No zip files found')
except Exception as e:
    print(f'[v0] Error: {str(e)}')
    import traceback
    traceback.print_exc()
