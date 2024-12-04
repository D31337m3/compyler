class PerformanceDashboard:
    def __init__(self):
        self.widgets = {
            'compilation_time': self._create_time_widget,
            'memory_usage': self._create_memory_widget,
            'error_rate': self._create_error_widget,
            'throughput': self._create_throughput_widget
        }
        
    def generate_dashboard(self, metrics):
        dashboard = {
            'timestamp': time.time(),
            'widgets': {}
        }
        
        for widget_name, widget_func in self.widgets.items():
            if widget_name in metrics:
                dashboard['widgets'][widget_name] = widget_func(metrics[widget_name])
                
        return dashboard
