class PerformanceReporter:
    def __init__(self, metrics_collector):
        self.collector = metrics_collector
        self.reports_dir = Path('performance_reports')
        self.reports_dir.mkdir(exist_ok=True)
        
    def generate_report(self, metrics):
        report = {
            'timestamp': time.time(),
            'metrics': metrics,
            'summary': self._generate_summary(metrics)
        }
        
        report_path = self.reports_dir / f'report_{int(time.time())}.json'
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
            
        return report_path
