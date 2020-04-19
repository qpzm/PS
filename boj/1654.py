from sys import stdin

N, K = map(int, stdin.readline().split())
rods = []
max_rod = 0

for _ in range(N):
    rod = int(stdin.readline())
    rods.append(rod)
    if rod > max_rod:
        max_rod = rod

def ok(piece):
    res = 0
    for rod in rods:
        res += rod // piece
        if res >= K:
            break

    if res >= K:
        return True


piece = 1
unit = max_rod // 2
while(unit >= 1):
    while(ok(piece + unit)):
        piece += unit
    unit = unit // 2
print(piece)
