def sol(s):
    l = []
    for c in s:
        if(c == '('):
            l.append(c)
        else:
            if not l:
                print('NO')
                return
            l.pop()
    if l:
        print('NO')
    else:
        print('YES')

N = int(input())
for _ in range(N):
    sol(input())
