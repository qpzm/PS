from math import sqrt
N = int(input())
D = [0, 1] + [100000] * (N-1)
for i in range(1, N+1):
    if int(sqrt(i)) ** 2 == i:
        D[i] = 1
    else:
        D[i] = min(list(1 + D[i - j**2] for j in range(1, int(sqrt(i)) + 1)))
print(D[N])
