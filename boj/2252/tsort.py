def main():
    N, M = list(map(int, input().split()))
    # Key is the vertex number starting from 1, not from 0.
    graph = dict()

    for _ in range(M):
        (src, dest) = tuple(map(int, input().split()))
        if src not in graph:
            graph[src] = [dest]
        else:
            graph[src].append(dest)

    dfs(graph, N)

def dfs(graph, N):
    result = []
    unvisited = set(range(1, N + 1))

    while(unvisited):
        v = unvisited.pop()
        rec_dfs(graph, v, unvisited, result)

    while(result):
        print(result.pop())

def rec_dfs(graph, v, unvisited, result):
    if v in unvisited:
        unvisited.remove(v)

    if v in graph:
        for u in graph[v]:
            if u in unvisited:
                rec_dfs(graph, u, unvisited, result)

    result.append(v)


if __name__ == '__main__':
    main()
