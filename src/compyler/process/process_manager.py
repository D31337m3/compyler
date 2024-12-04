class ProcessManager:
    def __init__(self, max_processes=None):
        self.max_processes = max_processes or cpu_count()
        self.active_processes = {}
        self.process_queue = Queue()
        
    def spawn_process(self, target, args=None):
        process_id = str(uuid.uuid4())
        process = Process(
            target=target,
            args=args or ()
        )
        self.active_processes[process_id] = process
        process.start()
        return process_id
