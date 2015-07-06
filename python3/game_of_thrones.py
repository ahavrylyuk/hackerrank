#! /usr/bin/env python


def is_anagram(chars):
    counts = [0] * (ord('z') - ord('a') + 1)
    for c in chars:
        counts[ord(c) - ord('a')] += 1
    has_odd = False
    for c in counts:
        if c % 2 == 1:
            if has_odd:
                return False
            has_odd = True
    return True

if __name__ == '__main__':
    print('YES' if is_anagram(input()) else 'NO')
