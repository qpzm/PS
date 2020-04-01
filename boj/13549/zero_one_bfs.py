from collections import deque

def solve(src, dest):
    end = max(dest + (dest - src) * 2 - 1, src)
    steps = [-1] * (end + 1)
    steps[src] = 0
    queue = deque([src])

    while queue:
        cur = queue.popleft()
        if cur == dest:
            return steps[cur]

        v = cur * 2
        if 0 <= v <= end and steps[v] == -1:
            steps[v] = steps[cur]
            queue.appendleft(v)

        for v in [cur - 1, cur + 1]:
            if 0 <= v <= end and steps[v] == -1:
                steps[v] = steps[cur] + 1
                queue.append(v)
