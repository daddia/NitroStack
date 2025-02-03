import redis
from time import time
import os

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

def rate_limiter(key, limit=5, window=60):
    current_time = int(time())
    window_start = current_time - (current_time % window)
    redis_key = f"rate_limit:{key}:{window_start}"

    current_count = redis_client.incr(redis_key)
    if current_count == 1:
        redis_client.expire(redis_key, window)

    if current_count > limit:
        raise Exception("Rate limit exceeded")
