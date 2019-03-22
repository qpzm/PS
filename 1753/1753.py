import heapq
import sys
INF = 999999999

def main():
    V, E = map(int, input().split())
    graph = dict()

    # convert to list index
    start = int(input()) - 1

    for _ in range(E):
        src, dest, weight = map(int, sys.stdin.readline().split())
        # convert to list index
        src, dest = src - 1, dest - 1
        if src in graph:
            graph[src].append((dest, weight))
        else:
            graph[src] = [(dest, weight)]

    print_dists(shortest_path(graph, V, start))

# Dijkstra algorithm using minheap
def shortest_path(graph, V, src):
    heap = [(0, src)]
    dists = [INF] * V

    while len(heap) > 0:
        nearest_dist, nearest = heapq.heappop(heap)

        # If min is not calculated yet
        if dists[nearest] == INF:
            dists[nearest] = nearest_dist
            if nearest in graph:
                for v, w in graph[nearest]:
                    new_dist = nearest_dist + w
                    if dists[v] == INF:
                        heapq.heappush(heap, (new_dist, v))

    return dists

def print_dists(dists):
    for d in dists:
        if d == INF:
            print('INF')
        else:
            print(d)

if __name__ == "__main__":
    main()
