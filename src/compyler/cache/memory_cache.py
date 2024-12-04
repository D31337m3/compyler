class MemoryCache:
    def __init__(self, max_size=1000):
        self.cache = OrderedDict()
        self.max_size = max_size
        
    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value  # Move to end (LRU)
            return value
        return None
        
    def set(self, key, value):
        if len(self.cache) >= self.max_size:
            self.cache.popitem(last=False)  # Remove oldest
        self.cache[key] = value
