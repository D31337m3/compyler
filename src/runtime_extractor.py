import tempfile
import zipfile
import os
import shutil

def extract_runtime(zip_path):
    # Add cleanup of temporary files
    temp_dir = None
    try:
        temp_dir = tempfile.mkdtemp()
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(temp_dir)
        # Use temp_dir...
    finally:
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
