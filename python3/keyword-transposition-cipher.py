def create_lookup(secret):
    seen = set()
    lookup = []
    for c in secret:
        if c in seen:
            continue
        lookup.append([c])
        seen.add(c)
    start, i = ord('A'), 0
    for c in map(chr, range(start, start + 26)):
        if c in seen:
            continue
        index = i % len(lookup)
        lookup[index].append(c)
        i += 1

    res = []
    for c in sorted(lookup, key=lambda c: c[0]):
        res.extend(c)
    return res


def reverse_lookup(lookup):
    res, start = ['']*26, ord('A')
    for i, c in enumerate(lookup):
        res[ord(c) - start] = chr(i + start)
    return res


def encipher(message, secret):
    lookup = reverse_lookup(create_lookup(secret))
    start, res = ord('A'), []
    for c in map(ord, message):
        res.append(chr(c) if c < start else lookup[c - start])
    return ''.join(res)

for _ in range(int(input())):
    secret, message = input(), input()
    print(encipher(message, secret))
