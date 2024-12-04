import socket
import threading
import pickle
from dataclasses import dataclass

@dataclass
class CompileTask:
    file_path: str
    code: bytes
    task_id: int

class DistributedCompiler:
    def __init__(self, host='0.0.0.0', port=6789):
        self.host = host
        self.port = port
        self.nodes = []
        
    def register_node(self, node_address):
        self.nodes.append(node_address)
        
    def distribute_tasks(self, tasks):
        for node in self.nodes:
            # Distribute compilation tasks across network
            yield self._send_task(node, tasks.pop())
            
    def _send_task(self, node, task):
        return f"Task {task.task_id} sent to {node}"
