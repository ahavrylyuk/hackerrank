#!/usr/bin/py


def lonelyinteger(a):
    cache = {}
    for v in a:
        count = cache.get(v, 0)
        cache[v] = count + 1
    return next(iter([k for k, v in cache.items() if v == 1]))


if __name__ == '__main__':
    #a = input()
    #b = map(int, raw_input().strip().split(" "))
    print(lonelyinteger([0, 0, 1, 2, 1]))
    assert lonelyinteger([0, 0, 1, 2, 1]) == 2, 'First'
    assert lonelyinteger([1, 2, 2, 2]) == 1, 'Second'
