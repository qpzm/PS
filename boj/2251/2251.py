from sys import stdin, stdout

buckets = list(map(int, stdin.readline().split()))
v = (0, 0, buckets[-1])
visited = set([v])

def dfs(current):
    for src in range(0, 3):
        for dest in range(0, 3):
            if src != dest:
                if current[src] >= buckets[dest] - current[dest]:
                    amount = buckets[dest] - current[dest]
                else:
                    amount = current[src]
                v = list(current)
                v[src]  -= amount
                v[dest] += amount
                v = tuple(v)
                if v[src] >= 0 and v[dest] >= 0 and v not in visited:
                    visited.add(v)
                    dfs(v)

dfs(v)
for i in sorted(set(list(u[2] for u in visited if u[0] == 0))):
    stdout.write(f'{i} ')
