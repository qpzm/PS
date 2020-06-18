from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(100_000)

def update_top_two(l, v):
    if l[0] < v:
        l = [v, l[0]]
    elif l[1] < v:
        l = [l[0], v]
    return l

def diameter(tree, v):
    visited = set()
    return _diameter(tree, visited, v)

def _diameter(tree, visited, v):
    visited.add(v)
    neighbors = list(filter(lambda t: t[0] not in visited, tree[v]))
    # A node in a tree has at least one neighbor
    # Case 0: No unvisited neighbor
    if(len(neighbors) == 0):
        return (0, 0)

    # Case 1: One neighbor
    if(len(neighbors) == 1):
        u, d = neighbors[0]
        local_max_diameter, local_max_radius = _diameter(tree, visited, u)
        return local_max_diameter, local_max_radius + d

    # Case 2: Two or more neighbors
    max_diameter = 0
    max_radiuses = [0, 0]
    for u, d in neighbors:
        local_max_diameter, local_max_radius = _diameter(tree, visited, u)
        max_diameter = max(max_diameter, local_max_diameter)
        max_radiuses = update_top_two(max_radiuses, local_max_radius + d)
    return max(sum(max_radiuses), max_diameter), max_radiuses[0]

def main():
    N = int(stdin.readline().rstrip())
    tree = defaultdict(list)
    for _ in range(N):
        v, *neighbors = list(map(int, stdin.readline().rstrip().split()))
        neighbors.pop() # Delete -1 at the end
        tree[v] = list(zip(neighbors[::2], neighbors[1::2]))
    # Reverse edge is already included in the input

    print(max(diameter(tree, 1)))

if __name__ == '__main__':
    main()
