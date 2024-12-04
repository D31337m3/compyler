import struct
import os
from pathlib import Path

class ExecutableBuilder:
    HEADER_MAGIC = b'CPYL'
    HEADER_VERSION = 1
    
    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        
    def build(self, compiled_path, runtime_path, output_path):
        with open(output_path, 'wb') as exe:
            # Write header
            self._write_header(exe)
            
            # Write runtime
            runtime_offset = exe.tell()
            runtime_size = self._write_runtime(exe, runtime_path)
            
            # Write compiled code
            code_offset = exe.tell()
            code_size = self._write_compiled_code(exe, compiled_path)
            
            # Update header with offsets
            self._update_header(exe, runtime_offset, runtime_size, 
                              code_offset, code_size)
    
    def _write_header(self, file):
        file.write(self.HEADER_MAGIC)
        file.write(struct.pack('<I', self.HEADER_VERSION))
        # Placeholder for offsets
        file.write(struct.pack('<QQQQ', 0, 0, 0, 0))
        
    def _write_runtime(self, file, runtime_path, chunk_size=8192):
        size = 0
        with open(runtime_path, 'rb') as runtime:
            while True:
                chunk = runtime.read(chunk_size)
                if not chunk:
                    break
                file.write(chunk)
                size += len(chunk)
                del chunk
        return size
