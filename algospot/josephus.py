import collections

def kill(k, q):
    q.popleft()
    # q rotates clockwise
    # q.popleft already rotates one slot.
    q.rotate(-(k-1))
    if len(q) == 2:
        return q
    return kill(k, q)

C = int(input())
for _ in range(C):
    N, K = map(int, input().split())
    q = collections.deque(range(1, N+1))
    print(" ".join(map(str, sorted(kill(K, q)))))
