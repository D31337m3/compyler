class CompilerThreadPool:
    def __init__(self, num_threads=None):
        self.pool = ThreadPoolExecutor(max_workers=num_threads)
        self.tasks = {}
        
    async def submit_task(self, task_func, *args):
        task_id = str(uuid.uuid4())
        future = self.pool.submit(task_func, *args)
        self.tasks[task_id] = future
        return task_id
        
    def get_result(self, task_id):
        if task_id in self.tasks:
            return self.tasks[task_id].result()
