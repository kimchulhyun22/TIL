import redis

REDIS_URL = '127.0.0.1'
REDIS_PORT = 6379
MAX_CONNECTION = 20


class RedisClient:
    def __init__(self):
        try:
            self.pool = redis.ConnectionPool(
                host=REDIS_URL, port=REDIS_PORT,
                max_connections=MAX_CONNECTION, db=0)

        except Exception as error:
            print(error)

    def get_connection(self):
        return redis.Redis(connection_pool=self.pool)

