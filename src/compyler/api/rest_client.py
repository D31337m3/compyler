class CompylerAPIClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
    async def submit_compilation(self, source_code):
        endpoint = f'{self.base_url}/compile'
        payload = {
            'source': source_code,
            'options': self.get_compilation_options()
        }
        return await self._make_request('POST', endpoint, payload)
