#!/usr/bin/evn python3

from collections import defaultdict
from itertools import chain


def shortest_path(g, start, goal):
    """ Complete BFS via MIT algorith

    g -> Graph represented via Adjacency list (Dict of sets)
    start -> start vertex
    goal -> end vertex

    Returns shortests path from start to goal
    """
    # level will contains shortest path for each vertex to start
    level = {start: 0}
    # parent will contains backtracks for each vertex to its parent
    parent = {start: None}
    i = 1
    frontier = [start]
    while frontier:
        next_f = []
        for u in frontier:
            for v in g[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next_f.append(v)
        frontier = next_f
        i += 1
    return level[goal] - 1


def read_line(line):
    return (map(int, x.split(',')) for x in line.split())

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        input()
        g = defaultdict(set)
        for i in range(1, 101):
            for j in range(i + 1, i + 7):
                g[i].add(j)
        for start, end in chain(read_line(input()), read_line(input())):
            g[start].add(end)
        print(shortest_path(g, 1, 100))
