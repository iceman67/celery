from tasks import collect, find


if __name__ == '__main__':
    result = collect.delay("s01", 10)
    result = collect.delay("s01", 11)
    result = collect.delay("s01", 9)
    print(result.get(timeout=1))

    result = find.delay("s01")
    print(result.get(timeout=1))
