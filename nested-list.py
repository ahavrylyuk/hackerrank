highest = 0
n = int(input())
students = []
for _ in range(n):
    name, score = input(), float(input())
    if score > highest:
        highest = score
    students.append([name, score])
lowest = second = highest
for name, score in students:
    if score < lowest:
        second = lowest
        lowest = score
    elif score < second and score != lowest:
        second = score
for n in sorted([s[0] for s in students if s[1] == second]):
    print(n)
