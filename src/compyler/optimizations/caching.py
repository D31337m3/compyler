import hashlib
import pickle
from pathlib import Path

class CompilationCache:
    def __init__(self, cache_dir='.compyler_cache'):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
    
    def get_cache_key(self, source_file):
        with open(source_file, 'rb') as f:
            content = f.read()
        return hashlib.sha256(content).hexdigest()
    
    def get_cached(self, source_file):
        cache_key = self.get_cache_key(source_file)
        cache_file = self.cache_dir / f"{cache_key}.cache"
        
        if cache_file.exists():
            with open(cache_file, 'rb') as f:
                return pickle.load(f)
        return None
