class WebSocketHandler:
    def __init__(self):
        self.connections = {}
        self.event_handlers = {
            'compilation_start': self._handle_compilation_start,
            'compilation_progress': self._handle_compilation_progress,
            'compilation_complete': self._handle_compilation_complete
        }
        
    async def handle_connection(self, websocket):
        connection_id = str(uuid.uuid4())
        self.connections[connection_id] = websocket
        
        try:
            await self._process_messages(websocket, connection_id)
        finally:
            del self.connections[connection_id]
