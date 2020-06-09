import redis
r = redis.Redis()

r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})

print(r.get("Bahamas"))
capitals = {}
capitals["Bahamas"] = "Nassau"
capitals["Croatia"] = "Zagreb"
capitals.get("Croatia")
capitals.get("Japan")  # None
