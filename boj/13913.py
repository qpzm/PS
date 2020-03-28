from collections import deque
from sys import stdin

MAX = 100_000

def solve(src, dest):
    steps = [-1] * (MAX + 1)
    queue = deque([src])
    steps[src] = src

    while queue:
        cur = queue.popleft()
        if cur == dest:
            break
        for v in [cur - 1, cur + 1, cur * 2]:
            if 0 <= v <= MAX and steps[v] == -1:
                steps[v] = cur
                queue.append(v)
    return(steps)

def calc_result(steps, dest):
    result = [dest]
    cnt = 0
    prev = steps[dest]
    while prev != dest:
        result.insert(0, prev)
        dest = prev
        prev = steps[dest]
        cnt += 1
    print(cnt)
    print(" ".join(map(str, result)))

src, dest = map(int, stdin.readline().split())
calc_result(solve(src, dest), dest)
