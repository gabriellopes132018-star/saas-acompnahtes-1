import os
import subprocess

try:
    # Use find command to locate escortwp.zip
    result = subprocess.run(['find', '/', '-name', 'escortwp.zip', '-type', 'f'], 
                          capture_output=True, text=True, timeout=10)
    
    if result.stdout:
        zip_paths = result.stdout.strip().split('\n')
        print('[v0] Found zip files:')
        for path in zip_paths:
            if path:
                print(f'  {path}')
    else:
        print('[v0] No zip files found')
        
except subprocess.TimeoutExpired:
    print('[v0] Search timed out')
except Exception as e:
    print(f'[v0] Error: {e}')
