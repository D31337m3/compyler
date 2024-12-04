import os
import sys
import subprocess
from pathlib import Path

def get_python_runtime():
    # Use context managers for subprocess to ensure proper cleanup
    try:
        with subprocess.Popen(['python3', '--version'], 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE) as proc:
            proc.communicate()
            return 'system'
    except FileNotFoundError:
        try:
            with subprocess.Popen(['python', '--version'],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE) as proc:
                proc.communicate()
                return 'system'
        except FileNotFoundError:
            pass

    runtime_zip = Path(__file__).parent / 'python_runtime_blob.zip'
    if runtime_zip.exists():
        return str(runtime_zip)
    
    if '--embed-runtime' in sys.argv:
        return 'embedded'
        
    raise RuntimeError('No Python runtime found')
def initialize_runtime():
    runtime_type = get_python_runtime()
    
    if runtime_type == 'system':
        return # Use system Python directly
        
    if runtime_type.endswith('.zip'):
        # Extract and use bundled runtime zip
        extract_runtime(runtime_type)
        return
        
    if runtime_type == 'embedded':
        # Use embedded blob only when requested
        extract_embedded_runtime()
        return