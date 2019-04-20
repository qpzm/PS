def top_parent(parent, v):
    p = parent[v]
    return (top_parent(parent, p) if p != v else p)


V, E = map(int, input().split())
weight_sum = 0
parent = list(range(V + 1)) # set representation with tree, first entry is dummy
graph = [tuple(map(int, input().split())) for _ in range(E)]
graph.sort(key=lambda x: x[2])
for u, v, w in graph:
    tu, tv = top_parent(parent, u), top_parent(parent, v)
    parent[u], parent[v] = tu, tv
    if tu != tv:
        parent[tv] = tu
        weight_sum += w
print(weight_sum)
