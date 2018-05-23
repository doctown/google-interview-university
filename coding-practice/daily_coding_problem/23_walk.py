"""
You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
"""


import collections


WALKABLE = 'f'
NON_WALKABLE = 't'


def walk(matrix, start, end):
    # only add if walkable
    q = collections.deque([(start, 0)])
    found = False

    while q and not found:
        (x, y), step = q.popleft()
        if (x, y) == end:
            found = True
        matrix[x][y] = NON_WALKABLE

        for next_x, next_y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= next_x < len(matrix) and 0 <= next_y < len(matrix[0]) and matrix[next_x][next_y] == WALKABLE:
                q.append(((next_x, next_y), step + 1))

    return step if found else None


def TestSuite():
    matrix = [['f', 'f', 'f', 'f'], ['t', 't', 'f', 't'], ['f', 'f', 'f', 'f'], ['f', 'f', 'f', 'f']]
    start = (3, 0)
    end = (0, 0)
    output = 7
    actual = walk(matrix, start, end)

    assert output == actual, "{} == {}".format(output, actual)

    matrix = [['f', 't', 'f', 'f'], ['t', 't', 'f', 't'], ['f', 'f', 'f', 'f'], ['f', 'f', 'f', 'f']]
    start = (3, 0)
    end = (0, 0)
    output = None
    actual = walk(matrix, start, end)

    assert output == actual, "{} == {}".format(output, actual)

    print("Done")

TestSuite()
