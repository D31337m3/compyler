class ReportGenerator:
    def __init__(self, template_dir="report_templates"):
        self.template_dir = Path(template_dir)
        self.report_types = {
            'performance': self._generate_performance_report,
            'compilation': self._generate_compilation_report,
            'error': self._generate_error_report
        }
        
    def generate_report(self, report_type, data):
        if report_type in self.report_types:
            return self.report_types[report_type](data)
