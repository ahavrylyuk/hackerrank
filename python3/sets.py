input()
s1 = set(int(x) for x in input().split())
input()
s2 = set(int(x) for x in input().split())
for e in sorted(s1 ^ s2):
    print(e)
