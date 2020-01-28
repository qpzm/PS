def hanoi(n, src, middle, dest):
    if n == 0:
        return
    else:
        hanoi(n - 1, src, dest, middle)
        print(src, dest)
        hanoi(n - 1, middle, src, dest)

N = int(input())
print(2 ** N - 1)
if N <= 20:
    hanoi(N, 1, 2, 3)
