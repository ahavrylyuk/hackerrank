values = set(int(x) for x in input().split())
missing = []
for i in range(min(values), max(values) + 1):
    if i not in values:
        if len(missing) and i - missing[-1][-1] is 1:
            missing[-1].append(i)
        else:
            missing.append([i])
res = ""
for rng in missing:
    value = None
    if len(rng) <= 2:
        value = ",".join(map(str, rng))
    else:
        value = "{0}-{1}".format(min(rng), max(rng))
    res += "{0}{1}".format("," if len(res) else "", value)

print(res)
