def sol(res, last, m):
    if m == 0:
        print(res)
    else:
        for i in range(last, N+1):
            res += f'{i} '
            sol(res, i, m-1)
            res = res[:-2]

N, M = map(int, input().split())
sol('', 1, M)
