class DistributedCache:
    def __init__(self, redis_url):
        self.redis_client = redis.from_url(redis_url)
        self.default_ttl = 3600  # 1 hour
        
    async def get_cached_result(self, key):
        result = await self.redis_client.get(key)
        if result:
            return pickle.loads(result)
        return None
        
    async def cache_result(self, key, value, ttl=None):
        ttl = ttl or self.default_ttl
        await self.redis_client.setex(
            key,
            ttl,
            pickle.dumps(value)
        )
