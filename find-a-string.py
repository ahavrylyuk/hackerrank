s = input()
pattern = input()
c = 0
for i in range(len(s)):
    if s[i:i + len(pattern)] == pattern:
        c += 1
print(c)
