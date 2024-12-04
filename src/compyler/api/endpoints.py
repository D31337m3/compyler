class APIEndpoints:
    def __init__(self, app):
        self.app = app
        self.setup_routes()
        
    def setup_routes(self):
        self.app.add_route('/compile', self.handle_compile)
        self.app.add_route('/status', self.handle_status)
        self.app.add_route('/metrics', self.handle_metrics)
        
    async def handle_compile(self, request):
        compilation_id = str(uuid.uuid4())
        task = asyncio.create_task(
            self._process_compilation(request.json, compilation_id)
        )
        return {'compilation_id': compilation_id}
