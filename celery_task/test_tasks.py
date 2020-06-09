from tasks import collect, find,cat

if __name__ == '__main__':
    result = collect.delay("alice", "alice.pem")
    print(result.get(timeout=1))

    result = find.delay("alice")
    print(result.get(timeout=1))

    
    hash_val = result.get(timeout=1)
    print(hash_val)
    result = cat.delay(hash_val)
    print(result.get(timeout=1))
