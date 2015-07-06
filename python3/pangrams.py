#! /usr/bin/env python


def is_pangram(s):
    chars = set()
    for code in map(ord, s):
        if code > 90:
            code -= 32
        if code > 32:
            chars.add(code)
    return len(chars) == 26


if __name__ == '__main__':
    print('pangram' if is_pangram(input()) else 'not pangram')
