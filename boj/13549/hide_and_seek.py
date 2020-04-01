from collections import deque
from sys import stdin

def solve(src, dest):
    end = max(dest * 2 - 1, src)
    steps = [-1] * (end + 1)
    steps[src] = 0
    queue = deque([src])

    while queue:
        cur = queue.popleft()
        if cur == dest:
            return steps[cur]

        if cur != 0:
            v = cur * 2
            while(0 <= v <= end and steps[v] == -1):
                steps[v] = steps[cur]
                queue.appendleft(v)
                v *= 2

        for v in [cur - 1, cur + 1]:
            while(0 <= v <= end and steps[v] == -1):
                steps[v] = steps[cur] + 1
                queue.append(v)
                if v == 0: break
                v *= 2

def main():
    src, dest = map(int, stdin.readline().split())
    print(solve(src, dest))

if __name__ == '__main__':
    main()
