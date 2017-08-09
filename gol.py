import time
import sys

def neighbors (point):
    x, y = point
    yield (x, y+1)
    yield (x, y-1)
    yield (x+1, y)
    yield (x-1, y)
    yield (x+1, y+1)
    yield (x-1, y+1)
    yield (x+1, y-1)
    yield (x-1, y-1)

def advance (board):
    new = set([])
    for point in board:
        num = 0
        for neighbor in neighbors(point):
            snum = 0
            for sneighbor in neighbors(neighbor):
                if sneighbor in board:
                    snum += 1
            if snum == 3 and neighbor:
                new.add(neighbor)
            if neighbor in board:
                num += 1
        if num == 2 or num == 3:
            new.add(point)
    return new

board = set([(0, 0), (1, -1), (1, -2), (0, -2), (-1, -2)])
# board = set([(0, 0), (1, 0), (0, -1), (1, -1)])
# board = set([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])
# board = set([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)])
# board = set([(0, 0), (0, 2), (3, 0), (1, 3), (2, 3), (3, 3), (4, 3), (4, 2), (4, 1)])
# board = set([(0, 0), (-50, -50)])
# board =set([(-2, 0), (0, 0), (1, 0), (4, 0), (-1, -2), (0, -1), (1, -3), (0, 4), (-4, 4), (-2, -3)])
# board = set([(0, 0), (1, 0), (2, -1), (0, -1), (0, -2), (-7, 0), (-8, 0), (-8, 1),
             # (-6, 1), (-6, 2), (-7, 2), (-15, 1), (-15, 2), (-16, 1), (-16, 2),
             # (6, 2), (6, 3), (7, 2), (8, 3), (8, 4), (7, 4), (18, 3), (18, 4),
             # (19, 3), (19, 4), (19, -3), (19, -4), (19, -5), (20, -3), (21, -4),
             # (8, -8), (8, -4), (9, -8), (9, -10), (9, -8)])
while True:
    if len(board) != 0:
        first = board.pop()
        board.add(first)
        ax, ay = first
        bx, by = first
        for point in board:
            x, y = point
            if x > ax:
                ax = x
            if y > ay:
                ay = y
            if x < bx:
                bx = x
            if y < by:
                by = y
    print('')
    for y in range(by, ay+1):
        for x in range(bx, ax+1):
            if (x, y) in board:
                print('#', end='')
            elif (0, 0) == (x, y):
                print('G', end='')
            else:
                print('"', end='')
        print('')
    board = advance(board)
    # time.sleep(.2)
    input()
