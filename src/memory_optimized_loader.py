import os
import sys
import tempfile
import zipfile
import shutil
from pathlib import Path
from contextlib import contextmanager

@contextmanager
def memory_tracked_extraction():
    temp_dir = None
    try:
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
    finally:
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

def extract_with_progress(zip_path, chunk_size=8192):
    with memory_tracked_extraction() as temp_dir:
        with zipfile.ZipFile(zip_path) as zf:
            for item in zf.filelist:
                with zf.open(item) as source:
                    target_path = os.path.join(temp_dir, item.filename)
                    os.makedirs(os.path.dirname(target_path), exist_ok=True)
                    with open(target_path, 'wb') as target:
                        while True:
                            chunk = source.read(chunk_size)
                            if not chunk:
                                break
                            target.write(chunk)
                            del chunk  # Explicit cleanup
    return temp_dir

def monitor_memory_usage():
    import psutil
    process = psutil.Process()
    return process.memory_info().rss / 1024 / 1024  # MB

class RuntimeManager:
    def __init__(self):
        self.temp_resources = []
        
    def cleanup(self):
        for resource in self.temp_resources:
            if os.path.exists(resource):
                if os.path.isdir(resource):
                    shutil.rmtree(resource)
                else:
                    os.remove(resource)
        self.temp_resources.clear()
        
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cleanup()

def extract_runtime(zip_path):
    with RuntimeManager() as rm:
        start_mem = monitor_memory_usage()
        
        temp_dir = extract_with_progress(zip_path)
        rm.temp_resources.append(temp_dir)
        
        end_mem = monitor_memory_usage()
        print(f"Memory usage: {end_mem - start_mem:.2f}MB")
        
        return temp_dir
