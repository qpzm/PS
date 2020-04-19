from sys import stdin

N, K = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))
max_tree = max(trees)

def ok(ax):
    res = 0
    for tree in trees:
        cut = tree - ax
        if cut > 0:
            res += cut
        if res >= K:
            break

    if res >= K:
        return True


piece = 0
unit = max_tree // 2
while(unit >= 1):
    while(ok(piece + unit)):
        piece += unit
    unit = unit // 2
print(piece)
