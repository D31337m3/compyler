class ResourceManager:
    def __init__(self):
        self.resources = {}
        self.limits = {
            'memory': 1024 * 1024 * 1024,  # 1GB
            'cpu': 0.75,  # 75% CPU usage
            'disk': 1024 * 1024 * 1024 * 10  # 10GB
        }
        
    def allocate_resource(self, resource_type, amount):
        if self._check_availability(resource_type, amount):
            self.resources[resource_type] = amount
            return True
        return False
