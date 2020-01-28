import heapq
import sys


def main():
    V, E = map(int, input().split())
    graph = dict()

    for _ in range(E):
        v1, v2, weight = map(int, sys.stdin.readline().split())
        # convert to list index
        v1, v2 = v1 - 1, v2 - 1
        insert_edge(graph, v1, v2, weight)
        insert_edge(graph, v2, v1, weight)

    print(prim(graph, V))

def insert_edge(graph, src, dest, weight):
    if src in graph:
        # heapq sorts based on the first elem
        graph[src].append((weight, dest))
    else:
        graph[src] = [(weight, dest)]

def prim(graph, num_vtx):
    sum = 0
    init = list(graph.keys())[0]
    reachable = [False] * num_vtx
    reachable[init] = True
    heap = graph[init]
    heapq.heapify(heap)

    while len(heap) > 0:
        min_weight, nearest = heapq.heappop(heap)

        if not reachable[nearest]:
            reachable[nearest] = True
            sum += min_weight
            if nearest in graph:
                for w, v in graph[nearest]:
                    if not reachable[v]:
                        heapq.heappush(heap, (w, v))

    return sum


if __name__ == "__main__":
    main()
