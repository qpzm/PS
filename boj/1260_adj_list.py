from sys import stdin, stdout
from collections import deque

def search(V, graph, DFS=True):
    visited = [False] * (N + 1) # visited[0] is just an offset
    q = deque([V])
    visited[V] = True

    while(q):
        if DFS:
            u = q.pop()
        else:
            u = q.popleft()
        stdout.write(f'{u} ')
        for neighbor in graph[u]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
    stdout.write('\n')

N, _, V = map(int, stdin.readline().split())
graph = [[] for _ in range(N+1)]
for line in stdin:
    u, v = map(int, line.split())
    graph[v].append(u)
    graph[u].append(v)

for neighbors in graph:
    neighbors.sort()

search(V, graph, DFS=True)
search(V, graph, DFS=False)
