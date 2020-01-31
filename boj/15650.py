def sol(res, last, m):
    if m == 0:
        print(res)
    for i in range(last+1, N+1):
        res += f'{i} '
        sol(res, i, m-1)
        res = res[:-2]

N, M = map(int, input().split())
sol('', 0, M)
