class AlertSystem:
    def __init__(self):
        self.thresholds = {
            'memory_usage': 90,  # percentage
            'compilation_time': 300,  # seconds
            'error_rate': 0.1  # 10%
        }
        
    def check_alerts(self, metrics):
        alerts = []
        for metric_name, threshold in self.thresholds.items():
            if metric_name in metrics:
                if self._is_threshold_exceeded(metrics[metric_name], threshold):
                    alerts.append(self._create_alert(metric_name, metrics[metric_name]))
        return alerts
