from typing import Dict, Type
from redis.asyncio.client import Redis as Async_Redis
from redis.asyncio.cluster import RedisCluster as Async_Redis_Cluster
from redis.client import Redis
from redis.cluster import RedisCluster
from redis.exceptions import RedisClusterException
from redis.connection import ConnectionPool, ClusterConnectionPool
REDIS_URI="redis://host:port/db"

class RedisClient:
    __async_cache: Dict[str, Async_Redis] = {}
    __cache: Dict[str, Redis] = {}
    __pool_cache: Dict[str, ConnectionPool] = {}
    __async_pool_cache: Dict[str, ConnectionPool] = {}

    @classmethod
    async def async_get_client(cls: Type["RedisClient"], uri: str = REDIS_URI, cache: bool = True) -> Async_Redis:
        if not cache:
            try:
                return Async_Redis_Cluster.from_url(uri, decode_responses=True)
            except Exception:
                return Async_Redis.from_url(uri, decode_responses=True)

        if uri in cls.__async_cache:
            return cls.__async_cache[uri]

        try:
            pool = ClusterConnectionPool.from_url(uri, decode_responses=True)
            client = Async_Redis_Cluster(connection_pool=pool)
            await client.cluster_info()
            cls.__async_pool_cache[uri] = pool
            cls.__async_cache[uri] = client
        except RedisClusterException:
            pool = ConnectionPool.from_url(uri, decode_responses=True)
            client = Async_Redis(connection_pool=pool)
            cls.__async_pool_cache[uri] = pool
            cls.__async_cache[uri] = client

        return cls.__async_cache[uri]

    @classmethod
    def get_client(cls: Type["RedisClient"], uri: str = REDIS_URI, cache: bool = True) -> Redis:
        if not cache:
            try:
                pool = ClusterConnectionPool.from_url(uri, decode_responses=True)
                return RedisCluster(connection_pool=pool)
            except Exception:
                pool = ConnectionPool.from_url(uri, decode_responses=True)
                return Redis(connection_pool=pool)

        if uri in cls.__cache:
            return cls.__cache[uri]

        try:
            pool = ClusterConnectionPool.from_url(uri, decode_responses=True)
            client = RedisCluster(connection_pool=pool)
            client.cluster_info()
            cls.__pool_cache[uri] = pool
            cls.__cache[uri] = client
        except RedisClusterException:
            pool = ConnectionPool.from_url(uri, decode_responses=True)
            client = Redis(connection_pool=pool)
            cls.__pool_cache[uri] = pool
            cls.__cache[uri] = client

        return cls.__cache[uri]


# redis_client = RedisClient.get_client("redis://:rediszpwd@10.3.0.5:6479/0")
redis_client = RedisClient.get_client()

if __name__ == "__main__":
    redis = redis_client
    redis.set("redis_key", "redis_key")
    print(redis)
    print(redis.keys())
    # import asyncio
    # async def test() -> None:
    #     client = await RedisClient.async_get_client("redis://192.168.100.208:6379/0")
    #     print(await client.keys())
    # asyncio.get_event_loop().run_until_complete(test())
