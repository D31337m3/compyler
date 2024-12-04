import hashlib
import pickle
import os

class CompilerCache:
    def __init__(self, cache_dir='.cache'):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
        
    def cache_key(self, source_code):
        return hashlib.sha256(source_code.encode()).hexdigest()
        
    def get_cached(self, file_path):
        with open(file_path, 'rb') as f:
            key = self.cache_key(f.read().decode())
        cache_path = os.path.join(self.cache_dir, key)
        return os.path.exists(cache_path)
        
    def store(self, key, compiled_data):
        path = os.path.join(self.cache_dir, key)
        with open(path, 'wb') as f:
            pickle.dump(compiled_data, f)
            
    def retrieve(self, key):
        path = os.path.join(self.cache_dir, key)
        if os.path.exists(path):
            with open(path, 'rb') as f:
                return pickle.load(f)
        return None