#!/usr/bin/env python3


def permute(lex, index):
    c = lex[index]
    for i in range(index - 1, -1, -1):
        if c <= lex[i]:
            continue
        lex[index], lex[i] = lex[i], c
        return i


def increase_lex(w):
    lex, index = [ord(c) for c in w], -1
    # print(lex)
    for i in range(len(lex) - 1, -1, -1):
        p = permute(lex, i)
        if p is not None:
            index = i
            break
    if index is -1:
        return None
    if index - p > 1:
        lex = lex[:p + 1] + sorted(lex[p + 1:])
    return ''.join(map(chr, lex))


t = int(input())
for _ in range(t):
    res = increase_lex(input())
    print(res if res else 'no answer')
