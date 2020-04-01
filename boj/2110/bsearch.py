from sys import stdin

def main():
    locs = []
    _, C = map(int, input().split())
    locs = [int(y) for y in stdin.read().splitlines()]
    print(solve(locs, C))

def solve(locs, C):
    locs.sort()
    bottom, end = 1, (locs[-1] - locs[0]) // (C - 1) + 1
    return(bsearch(bottom, end, lambda d: check(d, locs, C)))

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

def bsearch(s, e, f):
# [start, end)
    if e - s == 1:
        return s

    middle = (s + e) // 2
    if f(middle):
        return bsearch(middle, e, f)
    else:
        return bsearch(s, middle, f)

if __name__ == "__main__":
    main()
