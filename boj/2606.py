from collections import deque

N = int(input())
M = int(input())
adj = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

q = deque([0])
visited = [False] * N
visited[0] = True

while len(q) != 0:
    cur = q.popleft()
    for neighbor in adj[cur]:
        if not visited[neighbor]:
            visited[neighbor] = True
            q.append(neighbor)

print(visited.count(True) - 1)
