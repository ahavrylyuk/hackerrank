n = int(input())
lst = []
res = set(input())
for _ in range(n - 1):
    line = set(input())
    res = res.intersection(line)
print(len(res))
