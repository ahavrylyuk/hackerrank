input()
maximum = second = -100
for n in (int(x) for x in input().split()):
    if n > maximum:
        second, maximum = maximum, n
    elif n > second and n != maximum:
        second = n
print(second)
