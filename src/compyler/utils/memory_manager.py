import os
import psutil
import tempfile
import shutil
from contextlib import contextmanager

class RuntimeManager:
    def __init__(self):
        self.temp_dirs = []
        self.temp_files = []
        
    def create_temp_dir(self):
        temp_dir = tempfile.mkdtemp()
        self.temp_dirs.append(temp_dir)
        return temp_dir
        
    def create_temp_file(self, suffix=None):
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
        self.temp_files.append(temp_file.name)
        return temp_file.name
        
    def cleanup(self):
        for dir_path in self.temp_dirs:
            if os.path.exists(dir_path):
                shutil.rmtree(dir_path)
        
        for file_path in self.temp_files:
            if os.path.exists(file_path):
                os.unlink(file_path)
                
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cleanup()
