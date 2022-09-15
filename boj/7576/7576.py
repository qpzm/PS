from sys import stdin
from collections import deque

def checkDone(grids):
    rows = len(grids)
    cols = len(grids[0])
    for i in range(0, rows):
        for j in range(0, cols):
            if(grids[i][j] == 0):
                return False

    return True


def main():
    cols, rows = map(int, stdin.readline().split())
    grids = []
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    q = deque()
    max_day = 0

    for _ in range(0, rows):
        grids.append(list(map(int, stdin.readline().split())))

    for i in range(0, rows):
        for j in range(0, cols):
            if(grids[i][j] == 1):
                q.append((i, j, 0))

    while(len(q) != 0):
        (i, j, day) = q.popleft();
        for k, l in directions:
            next_i, next_j = i + k, j + l
            if (0 <= next_i < rows and 0 <= next_j >= 0 and next_j < cols and grids[next_i][next_j] == 0):
                grids[next_i][next_j] = 1
                q.append((next_i, next_j, day + 1))
                max_day = day + 1

    if (checkDone(grids)):
        print(max_day)
    else:
        print(-1)


if __name__ == '__main__':
    main()

