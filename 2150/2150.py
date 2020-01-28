# sys.stdin.readline()으로 읽으니 런타임에러가 계속 발생
# 오래된 데이터에 \n이 없는 경우가 있다고 함.
# https://www.acmicpc.net/blog/view/70
import sys
sys.setrecursionlimit(10**9)

def dfs(graph, V, stack):
    vertices = []
    # 0 white 1 gray 2 black
    colors = [0] * (V + 1)
    while(stack):
        u = stack[-1]
        if colors[u] == 0:
            colors[u] = 1
            if u in graph:
                for v in graph[u]:
                    if colors[v] == 0:
                        stack.append(v)
        elif colors[u] == 1:
            v = stack.pop()
            vertices.append(v)
            colors[v] = 2
        else:
            stack.pop()
    return vertices

def dfs_visit(u, graph, visited, vertices):
    visited[u] = True
    if u in graph:
        for v in graph[u]:
            if not visited[v]:
                dfs_visit(v, graph, visited, vertices)
    vertices.append(u)

def dfs2(graph, visited, order):
    answer = []
    for u in order:
        if not visited[u]:
            vertices = []
            dfs_visit(u, graph, visited, vertices)
            answer.append(sorted(vertices))
    return answer


V, E = [int(x) for x in input().split()]
graph, trans = {}, {}

for _ in range(E):
    u, v = tuple(map(int, input().split()))
    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]
    if v in trans:
        trans[v].append(u)
    else:
        trans[v] = [u]

vertices = dfs(graph, V, list(range(1, V+1)))
vertices = list(reversed(vertices))
answer = dfs2(trans, [False] * (V + 1), vertices)
answer = sorted(answer, key=lambda x: x[0])
print(len(answer))
for l in answer:
    print(' '.join(map(str, l + [-1])))
