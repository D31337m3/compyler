class CacheManager:
    def __init__(self, cache_dir="cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        self.max_cache_size = 1024 * 1024 * 100  # 100MB
        
    def get_cached_compilation(self, source_hash):
        cache_path = self.cache_dir / source_hash
        if cache_path.exists():
            return self._load_cache(cache_path)
        return None
        
    def cache_compilation(self, source_hash, compilation_result):
        cache_path = self.cache_dir / source_hash
        self._save_cache(cache_path, compilation_result)
