import aioredis

import config


class Cache(object):

    MIN_POOL_CONNS = 3
    MAX_POOL_CONNS = 5

    def __init__(self):
        self._pool = None

    async def _create_pool(self):
        self._pool = await aioredis.create_redis_pool(
            config.REDIS_URI,
            minsize=self.MIN_POOL_CONNS,
            maxsize=self.MAX_POOL_CONNS,
        )

    async def set(self, key, value):
        # Add json serialization-deserialization
        return await self._pool.set(key, value)

    async def get(self, key):
        return await self._pool.get(key)

    async def close(self):
        self._pool.close()
        await self._pool.wait_closed()
