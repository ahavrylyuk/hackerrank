x, y, z, n = (int(input()) for _ in range(4))
res = [
        [xi, yi, zi]
        for xi in range(x + 1)
        for yi in range(y + 1)
        for zi in range(z + 1)
        if sum((xi, yi, zi)) != n
    ]
print(res)
