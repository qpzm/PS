from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().strip().split())
maze = []
i, j = 0, 0
for _ in range(N):
    maze.append([int(char) for char in stdin.readline().strip()])
dists = [[-1] * M for _ in range(N)]
dists[0][0] = 1
q  = deque([(0,0)])
while(len(q) != 0):
    i, j = q.popleft()
    if i == N-1 and j == M-1:
        break
    for u, v in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if 0<= u < N and 0<= v < M and dists[u][v] == -1 and maze[u][v] != 0:
            q.append((u, v))
            dists[u][v] = dists[i][j] + 1

print(dists[N-1][M-1])
