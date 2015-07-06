n = int(input())
a = [int(x) for x in input().split()]
for c in (
    sum(1 for x in a if x > 0),
    sum(1 for x in a if x < 0),
    sum(1 for x in a if x is 0)
):
    print("{:.3f}".format(c / n))
