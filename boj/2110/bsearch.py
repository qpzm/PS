from sys import stdin
from math import floor
input = stdin.readline

def main():
    locs = []
    N, C = map(int, input().split())
    for _ in range(N):
        locs.append(int(input().rstrip()))
    print(solve(locs, C))

def solve(locs, C):
    locs = sorted(locs)
    init_dist = floor((locs[-1] - locs[0]) / (C - 1))
    return(bsearch(1, init_dist, locs, C))

def check(dist, locs, cnt):
    # put one router at the start
    routers, limit = cnt - 1, locs[0] + dist

    for loc in locs[1:]:
        if loc < limit:
            continue
        if routers > 0:
            limit = loc + dist
            routers -= 1
        if routers == 0:
            break

    return routers == 0

def bsearch(s, e, locs, cnt):
    if e == s:
        return e

    if e - s == 1:
        if check(e, locs, cnt):
            return e
        else:
            return s

    middle = floor((s + e) / 2)
    if check(middle, locs, cnt):
        return bsearch(middle, e, locs, cnt)
    else:
        return bsearch(s, middle - 1, locs, cnt)

if __name__ == "__main__":
    main()
