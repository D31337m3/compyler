from concurrent.futures import ThreadPoolExecutor
import os

class CompilerThreading:
    def __init__(self, max_workers=4):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.tasks = []
        
    def compile_parallel(self, files):
        for file in files:
            future = self.executor.submit(self._compile_single, file)
            self.tasks.append(future)
        return self.tasks
    
    def _compile_single(self, file):
        return f"Compiled {file}"