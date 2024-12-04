class BenchmarkSuite:
    def __init__(self):
        self.benchmarks = []
        self.metrics = defaultdict(list)
        
    def add_benchmark(self, name, test_func):
        self.benchmarks.append({
            'name': name,
            'func': test_func
        })
        
    def run_benchmarks(self, iterations=3):
        for benchmark in self.benchmarks:
            times = []
            for _ in range(iterations):
                start_time = time.perf_counter()
                benchmark['func']()
                elapsed = time.perf_counter() - start_time
                times.append(elapsed)
            
            self.metrics[benchmark['name']] = {
                'avg_time': statistics.mean(times),
                'min_time': min(times),
                'max_time': max(times)
            }
