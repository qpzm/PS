from sys import stdin, stdout
from collections import deque

N, _, V = map(int, stdin.readline().split())
graph = dict()
for line in stdin:
    u, v = map(int, line.split())
    if v not in graph:
        graph[v] = [u]
    else:
        graph[v].append(u)

    if u not in graph:
        graph[u] = [v]
    else:
        graph[u].append(v)

for neighbors in graph.values():
    neighbors.sort()

def dfs(V, graph):
    visited = [False] * (N + 1) # visited[0] is just an offset
    _dfs(visited, V)
    stdout.write('\n')

def _dfs(visited, V):
    if not visited[V]:
        visited[V] = True
        stdout.write(f'{V} ')
        if V in graph:
            for neighbor in graph[V]:
                _dfs(visited, neighbor)

def bfs(V, graph):
    visited = [False] * (N + 1)
    q = deque([V])
    visited[V] = True

    while(q):
        u = q.popleft()
        stdout.write(f'{u} ')
        if u in graph:
            for neighbor in graph[u]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
    stdout.write('\n')

dfs(V, graph)
bfs(V, graph)
