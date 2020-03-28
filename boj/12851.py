from collections import deque
from sys import stdin

MAX = 100_000

def solve(src, dest):
    visited = [False] * (MAX + 1)
    queue = deque([src])
    step = 0
    cnt = 0

    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            visited[cur] = True
            if cur == dest:
                cnt += 1
            elif cnt == 0:
                for v in [cur - 1, cur + 1, cur * 2]:
                    if 0 <= v <= MAX and not visited[v]:
                        queue.append(v)
        if cnt != 0:
            break
        step += 1

    print(step)
    print(cnt)

src, dest = map(int, stdin.readline().split())
solve(src, dest)
