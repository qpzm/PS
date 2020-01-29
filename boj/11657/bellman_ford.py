from sys import stdin, stdout
from math import inf, isinf

def relax(e):
    src, dest, dist = e
    relaxed = False
    if D[dest] > D[src] + dist:
        D[dest] = D[src] + dist
        relaxed = True
    return relaxed

def bf(E):
    for _ in range(N-1):
        for e in E:
            relax(e)

    # check if a negative cycle exists
    for e in E:
        if relax(e):
            return False
    return True

N, M = map(int, input().split())
D = [0] + [inf] * (N-1)
E = []
for _ in range(M):
    src, dest, dist = map(int, stdin.readline().split())
    E.append((src-1 , dest-1, dist))

if bf(E):
    for d in D[1:]:
        if isinf(d):
            d = -1
        stdout.write(str(d) + '\n')
else:
    print(-1)
