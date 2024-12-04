class BuildMonitor:
    def __init__(self):
        self.build_history = []
        self.metrics = defaultdict(list)
        
    def monitor_build(self, build_func):
        build_info = {
            'id': uuid.uuid4(),
            'start_time': time.time(),
            'metrics': {}
        }
        
        try:
            result = build_func()
            build_info['status'] = 'success'
            build_info['result'] = result
        except Exception as e:
            build_info['status'] = 'failure'
            build_info['error'] = str(e)
