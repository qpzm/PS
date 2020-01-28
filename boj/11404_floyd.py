import sys

def floyd(W):
    n = len(W)
    D = W
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] is None or D[k][j] is None:
                    continue
                if D[i][j] is None or D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
    return D

N = int(input())
M = int(input())
W = [[None] * N for _ in range(N)]
for _ in range(M):
    src, dest, dist = map(int, sys.stdin.readline().split())
    src, dest = src-1, dest-1
    if W[src][dest] is None or W[src][dest] > dist:
        W[src][dest] = dist

# 같은 도시간 거리는 0, 이 조건이 명시되어 있지는 않은데 출력 보면 필요
for i in range(N):
    W[i][i] = 0

D = floyd(W)
for i in range(N):
    for j in range(N):
        if D[i][j] is None:
            D[i][j] = 0

for row in D:
    print(" ".join(map(str, row)))
