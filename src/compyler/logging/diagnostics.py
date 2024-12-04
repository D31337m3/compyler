class DiagnosticsCollector:
    def __init__(self):
        self.collectors = {
            'system': self._collect_system_info,
            'process': self._collect_process_info,
            'compilation': self._collect_compilation_info
        }
        
    def collect_diagnostics(self):
        diagnostics = {}
        for name, collector in self.collectors.items():
            diagnostics[name] = collector()
        return diagnostics
