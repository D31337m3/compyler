import time
import statistics
from pathlib import Path
from compyler.core.compiler import Compiler

class CompilerBenchmark:
    def __init__(self, test_files_dir="benchmark_samples"):
        self.test_files = Path(test_files_dir).glob("*.py")
        self.results = []
        
    def run_benchmarks(self, iterations=5):
        for test_file in self.test_files:
            times = []
            for _ in range(iterations):
                start_time = time.perf_counter()
                compiler = Compiler(test_file)
                compiler.compile()
                end_time = time.perf_counter()
                times.append(end_time - start_time)
                
            self.results.append({
                'file': test_file.name,
                'avg_time': statistics.mean(times),
                'std_dev': statistics.stdev(times),
                'min_time': min(times),
                'max_time': max(times)
            })
