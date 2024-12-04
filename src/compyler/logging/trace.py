class TraceManager:
    def __init__(self):
        self.traces = []
        self.current_trace = None
        
    def start_trace(self, operation):
        self.current_trace = {
            'operation': operation,
            'start_time': time.time(),
            'events': []
        }
        
    def add_event(self, event_type, data):
        if self.current_trace:
            self.current_trace['events'].append({
                'type': event_type,
                'timestamp': time.time(),
                'data': data
            })
