class TaskScheduler:
    def __init__(self):
        self.scheduled_tasks = {}
        self.running = False
        
    def schedule_task(self, task, interval):
        task_id = str(uuid.uuid4())
        self.scheduled_tasks[task_id] = {
            'task': task,
            'interval': interval,
            'last_run': None
        }
        return task_id
        
    def start(self):
        self.running = True
        while self.running:
            self._execute_due_tasks()
            time.sleep(1)
