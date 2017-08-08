import time

def neighbors (point):
    x, y = point
    return [(x, y+1),
            (x, y-1),
            (x+1, y),
            (x-1, y),
            (x+1, y+1),
            (x-1, y+1),
            (x+1, y-1),
            (x-1, y-1)]

def advance (board):
    new = set([])
    for point in board:
        nbrs = neighbors(point)
        num = 0
        for neighbor in nbrs:
            sneighbors = neighbors(neighbor)
            snum = 0
            for sneighbor in sneighbors:
                if sneighbor in board:
                    snum += 1
            if snum == 3 and neighbor:
                new.add(neighbor)
            if neighbor in board:
                num += 1
        if num == 2 or num == 3:
            new.add(point)
    return list(new)

# board = [(0, 0), (1, -1), (1, -2), (0, -2), (-1, -2)]
# board = [(0, 0), (1, 0), (0, -1), (1, -1)]
# board = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
# board = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
board = [(0, 0), (0, 2), (3, 0), (1, 3), (2, 3), (3, 3), (4, 3), (4, 2), (4, 1)]
while True:
    for j in range(-20, 20):
        for i in range(-50, 50):
            if (i, j) in board:
                print('0', end='')
            else:
                print('.', end='')
        print('')
    board = advance(board)
    time.sleep(.2)
