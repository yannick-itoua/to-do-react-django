import redis

try:
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.ping()
    print("Redis is working!")
except redis.ConnectionError as e:
    print(f"Redis connection failed: {e}")
