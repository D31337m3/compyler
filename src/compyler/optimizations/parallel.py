from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count

class ParallelCompiler:
    def __init__(self, max_workers=None):
        self.max_workers = max_workers or cpu_count()
    
    def compile_multiple(self, source_files):
        with ProcessPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [
                executor.submit(self._compile_single, src)
                for src in source_files
            ]
            return [f.result() for f in futures]
            
    def _compile_single(self, source_file):
        from ..core.compiler import Compiler
        compiler = Compiler(source_file)
        return compiler.compile()
