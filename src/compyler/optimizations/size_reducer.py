class ExecutableSizeReducer:
    def __init__(self):
        self.compression_methods = {
            'strip': self._strip_debug_info,
            'compress': self._compress_bytecode,
            'deduplicate': self._deduplicate_strings
        }
        
    def reduce_size(self, executable_path):
        original_size = os.path.getsize(executable_path)
        
        for method in self.compression_methods.values():
            method(executable_path)
            
        final_size = os.path.getsize(executable_path)
        return original_size - final_size
