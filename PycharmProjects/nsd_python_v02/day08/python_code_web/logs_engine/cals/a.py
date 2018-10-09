import redis
r = redis.Redis(host='192.168.99.100', port=46379)

print r.get("xm")
r.set("xm","mcm")