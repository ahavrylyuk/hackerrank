#! /usr/bin/env python


def get_team(n, m, person):
    teams = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            teams.append(bin(person[i] | person[j]).count('1'))
    max_topic = max(teams)
    return (max_topic, teams.count(max_topic))


if __name__ == '__main__':
    n, m = map(int, input().split())
    person = [int(x, 2) for x in [input() for _ in range(n)]]
    team = get_team(n, m, person)
    print(team[0])
    print(team[1])
