MAX = 100_000

def check_and_append(q, visited, pos):
    if pos >= 0 and pos <= MAX and not visited[pos]:
        visited[pos] = True
        q.append(pos)

def main():
    src, dest = map(int, input().split())
    visited = [False] * (MAX + 1)
    queue = [src]
    step = 0

    while(len(queue) != 0):
        for _ in range(len(queue)):
            cur = queue.pop(0)
            visited[cur] = True
            if cur == dest:
                print(step)
                return
            check_and_append(queue, visited, cur - 1)
            if dest > cur:
                check_and_append(queue, visited, cur + 1)
                check_and_append(queue, visited, cur * 2)
        step += 1

if __name__ == '__main__':
    main()
