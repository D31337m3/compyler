import os
import sys
import subprocess
from pathlib import Path
from ..utils.memory_manager import RuntimeManager

class RuntimeLoader:
    def __init__(self):
        self.runtime_dir = Path(__file__).parent.parent / 'runtime'
        self.runtime_zip = self.runtime_dir / 'python_runtime_blob.zip'
        
    def get_runtime(self, embed_runtime=False):
        if embed_runtime:
            return self._get_embedded_runtime()
            
        # Try system Python first
        system_python = self._find_system_python()
        if system_python:
            return system_python
            
        # Try external runtime zip
        if self.runtime_zip.exists():
            return self._extract_runtime_zip()
            
        raise RuntimeError("No suitable Python runtime found")
        
    def _find_system_python(self):
        try:
            with subprocess.Popen(['python3', '--version'], 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE) as proc:
                proc.communicate()
                return 'python3'
        except FileNotFoundError:
            try:
                with subprocess.Popen(['python', '--version'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE) as proc:
                    proc.communicate()
                    return 'python'
            except FileNotFoundError:
                return None
