from collections import deque
from sys import stdin

MAX = 100_000

def solve(src, dest):
    steps = [0] * (MAX + 1)
    queue = deque([src])

    while queue:
        cur = queue.popleft()
        if cur == dest:
            return steps[cur]
        for v in [cur - 1, cur + 1, cur * 2]:
            if 0 <= v  <= MAX and steps[v] == 0:
                steps[v] = steps[cur] + 1
                queue.append(v)

src, dest = map(int, stdin.readline().split())
print(solve(src, dest))
