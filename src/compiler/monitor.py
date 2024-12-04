import time
import psutil
from dataclasses import dataclass

@dataclass
class CompilerMetrics:
    cpu_usage: float
    memory_usage: float
    compilation_time: float
    files_processed: int

class PerformanceMonitor:
    def __init__(self):
        self.start_time = time.time()
        self.metrics = CompilerMetrics(0.0, 0.0, 0.0, 0)
    
    def update_metrics(self):
        self.metrics.cpu_usage = psutil.cpu_percent()
        self.metrics.memory_usage = psutil.Process().memory_info().rss / 1024 / 1024
        self.metrics.compilation_time = time.time() - self.start_time