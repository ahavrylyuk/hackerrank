from re import search
pattern = 'hackerrank'
for _ in range(int(input())):
    sentence = input()
    begin = search('^' + pattern, sentence)
    end = search(pattern + '$', sentence)
    if begin and end:
        print(0)
    elif begin:
        print(1)
    elif end:
        print(2)
    else:
        print(-1)
