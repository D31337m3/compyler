import time
import psutil
from collections import defaultdict

class PerformanceTracker:
    def __init__(self):
        self.metrics = defaultdict(list)
        self.start_time = None
        
    def start_tracking(self):
        self.start_time = time.perf_counter()
        self.process = psutil.Process()
        
    def record_metric(self, name, value):
        self.metrics[name].append({
            'value': value,
            'timestamp': time.perf_counter() - self.start_time
        })
