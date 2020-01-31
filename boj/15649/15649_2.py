def solve(res, m):
    if m == 0:
        print(res)
    for i in range(1, N+1):
        if not used[i]:
            used[i] = True
            res += f'{i} '
            solve(res, m-1)
            res = res[:-2]
            used[i] = False

N, M = map(int, input().split())
res = ''
used = [False] * (N+1)
solve(res, M)
