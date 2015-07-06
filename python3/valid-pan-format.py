from re import search
for _ in range(int(input())):
    print('YES' if search(r'^[A-Z]{5}[0-9]{4}[A-Z]$', input()) else 'NO')
