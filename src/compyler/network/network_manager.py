class NetworkManager:
    def __init__(self):
        self.connections = {}
        self.retries = 3
        
    async def send_request(self, url, method='GET', data=None):
        async with aiohttp.ClientSession() as session:
            for attempt in range(self.retries):
                try:
                    async with session.request(method, url, json=data) as response:
                        return await response.json()
                except Exception as e:
                    if attempt == self.retries - 1:
                        raise
