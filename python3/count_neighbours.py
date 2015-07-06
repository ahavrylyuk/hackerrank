#! /usr/bin/env python


def count_neighbours(grid, h, w):
    grid_len, line_len = len(grid), len(grid[0])
    line_range = [y for y in range(h - 1, h + 2) if y >= 0 and y < grid_len]
    row_range = [x for x in range(w - 1, w + 2) if x >= 0 and x < line_len]
    sum_all = sum([grid[y][x] for x in row_range for y in line_range])
    return sum_all - grid[h][w]


if __name__ == '__main__':
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
    assert count_neighbours(((1, 0, 1, 0, 1),
                             (0, 1, 0, 1, 0),
                             (1, 0, 1, 0, 1),
                             (0, 1, 0, 1, 0),
                             (1, 0, 1, 0, 1),
                             (0, 1, 0, 1, 0),), 5, 4) == 2
