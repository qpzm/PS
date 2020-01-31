def sol(res, m):
    if m == 0:
        print(res)
    else:
        for i in range(1, N+1):
            res += f'{i} '
            sol(res, m-1)
            res = res[:-2]

N, M = map(int, input().split())
sol('', M)
