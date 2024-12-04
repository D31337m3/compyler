class MetricCollector:
    def __init__(self, storage_backend='sqlite'):
        self.storage = self._init_storage(storage_backend)
        self.collectors = {
            'performance': self._collect_performance_metrics,
            'memory': self._collect_memory_metrics,
            'errors': self._collect_error_metrics
        }
        
    def collect_metrics(self):
        metrics = {}
        for name, collector in self.collectors.items():
            metrics[name] = collector()
        return metrics
