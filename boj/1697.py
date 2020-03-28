MAX = 100_000

def main():
    src, dest = map(int, input().split())
    queue = [(src, 0)]
    visited = [False] * (MAX + 1)

    for cur, step in queue:
        candidates = []
        visited[cur] = True
        if cur == dest:
            print(step)
            break
        if dest > cur:
            if cur - 1 >= 0:
                candidates.append(cur - 1)
            if cur + 1 <= MAX:
                candidates.append(cur + 1)
            if cur * 2 <= MAX:
                candidates.append(cur * 2)
        else:
            if cur - 1 >= 0:
                candidates.append(cur - 1)

        for node in candidates:
            if not visited[node]:
                queue.append((node, step + 1))

if __name__ == '__main__':
    main()
