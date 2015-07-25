_, source, key = input(), input(), int(input())
values = [''] * len(source)
for index, c in enumerate(source):
    values[index] = c
    if not c.isalpha():
        continue
    base = ord('A') if c.isupper() else ord('a')
    enc = (ord(c) - base + key) % 26 + base
    values[index] = chr(enc)
print(''.join(values))
