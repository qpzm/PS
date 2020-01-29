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
    no_neg_cycle = True
    for _ in range(N-1):
        relaxed = False
        for e in E:
            # Wrong! `or` is short-circuit operator
            # relaxed = relaxed or relax(e)
            relaxed = relax(e) or relaxed
        if not relaxed:
            return no_neg_cycle

    # check if a negative cycle exists
    for e in E:
        if relax(e):
            no_neg_cycle = False
            break

    return no_neg_cycle

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
