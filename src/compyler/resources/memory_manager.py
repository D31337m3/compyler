class MemoryManager:
    def __init__(self):
        self.allocated = {}
        self.peak_usage = 0
        
    def allocate(self, size, identifier):
        current_usage = self.get_current_usage()
        if current_usage + size <= self.get_max_memory():
            self.allocated[identifier] = size
            self.peak_usage = max(self.peak_usage, current_usage + size)
            return True
        return False
