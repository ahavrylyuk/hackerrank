#! /usr/bin/env python


def checkio(value):
    numbers = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}    
    ten = {1:'ten', 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
    first_ten = {0: 'ten', 1:'eleven', 2:'twelve', 3:'thirteen', 4:'fourteen', 5:'fifteen', 6:'sixteen', 7:'seventeen', 8:'eighteen', 9:'nineteen'}
    dividers = {1000: 'thousand', 100: 'hundred'}
    result = ''
    add_space = lambda s: ' ' if s else ''

    for divider, text in dividers.items():
        counts = value // divider
        value = value % divider
        if counts:
            result += add_space(result) + ' '.join([numbers[counts], text])
    ten_count = value // 10
    value = value % 10
    if ten_count == 1:
        result += add_space(result) + first_ten[value]
        value = 0
    elif ten_count:
        result += add_space(result) + ten[ten_count]
    if value:
        result += add_space(result) + numbers[value]
    return result if result else 'zero'


if __name__ == '__main__':
    for i in range(10000):
        print(checkio(i))

    #assert checkio(4)=='four'
    #assert checkio(143)=='one hundred forty three'
    #assert checkio(12)=='twelve'
    #assert checkio(101)=='one hundred one'
    #assert checkio(212)=='two hundred twelve'
    #assert checkio(40)=='forty'
