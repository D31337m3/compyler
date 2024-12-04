class MetricsCollector:
    def __init__(self):
        self.performance_data = defaultdict(list)
        
    def collect_compilation_metrics(self, source_file):
        metrics = {
            'compilation_time': self._measure_compilation_time(),
            'memory_usage': self._measure_memory_usage(),
            'file_size': self._get_file_size(source_file),
            'cpu_usage': self._measure_cpu_usage()
        }
        return metrics
        
    def _measure_compilation_time(self):
        start = time.perf_counter()
        yield
        return time.perf_counter() - start
