T = int(input())
for _ in range(T):
    N = int(input())
    D = [1, 1, 1, 2, 2]
    if N < 5:
        print(D[N-1])
    else:
        for _ in range(N-5):
            D.append(D[0] + D[4])
            del D[0]
        print(D[4])
