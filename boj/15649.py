def sol(acc, l):
    if len(acc) == M:
        print(' '.join(map(str, acc)))
    for i in range(len(l)):
        r = l.copy()
        x = r.pop(i)
        sol(acc + [x], r)

N, M = map(int, input().split())
l = list(range(1, N+1))
sol([], l)
