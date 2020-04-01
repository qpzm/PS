from collections import deque
from sys import stdin

def visit_all(v, steps, queue, steps_to_v):
    end = len(steps) - 1
    while(0 <= v <= end and steps[v] == -1):
        steps[v] = steps_to_v
        queue.append(v)
        v *= 2

def solve(src, dest):
    end = max(dest + (dest - src) * 2 - 1, src)
    steps = [-1] * (end + 1)
    steps[src] = 0
    queue = deque([src])
    visit_all(src * 2, steps, queue, steps[src])

    while queue:
        cur = queue.popleft()
        if cur == dest:
            return steps[cur]

        for v in [cur - 1, cur + 1]:
            visit_all(v, steps, queue, steps[cur] + 1)

def main():
    src, dest = map(int, stdin.readline().split())
    print(solve(src, dest))

if __name__ == '__main__':
    main()
