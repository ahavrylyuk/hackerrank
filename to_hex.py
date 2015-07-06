hex_numbers = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def to_hex(a, base=16):
    reminders = []
    while a > 0:
        reminder = a % base
        reminders.insert(0, hex_numbers.get(reminder, str(reminder)))
        a = a // base
    return ''.join(reminders)


for i in range(1000):
    print(to_hex(i))
