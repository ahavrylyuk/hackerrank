def is_funny(s):
    codes = [ord(c) for c in s]
    codes_len = len(codes)
    for i in range(codes_len - 1):
        d1 = codes[i + 1] - codes[i]
        d2 = codes[-(i + 1)] - codes[-(i + 2)]
        if abs(d1) != abs(d2):
            return False
    return True

t = int(input())
for _ in range(t):
    print('Funny' if is_funny(input()) else 'Not Funny')
