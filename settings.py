import redis
from string import ascii_letters, digits
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
db = redis.Redis(connection_pool=pool)

printable = ascii_letters + digits