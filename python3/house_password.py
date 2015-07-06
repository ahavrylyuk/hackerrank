#! /usr/bin/env python


def checkio(data):
    hasDigist = any([x.isdigit() for x in data])
    hasUpper = any([x.isupper() for x in data])
    hasLower = any([x.islower() for x in data])
    return bool(len(data) >= 10 and hasDigist and hasUpper and hasLower)


if __name__ == '__main__':
    assert checkio('A1213pokl') is False
    assert checkio('bAse730onE') is True
    assert checkio('asasasasasasasaas') is False
    assert checkio('QWERTYqwerty') is False
    assert checkio('123456123456') is False
    assert checkio('QwErTy911poqqqq') is True
