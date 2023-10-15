# Fenwick Tree
# 5 101 [5, 5] 5
# 4 100 [1, 4] 10
# 3  11 [3, 3] 3
# 2  10 [1, 2] 3
# 1   1 [1, 1] 1
class FenwickTree:
    def __init__(self, n):
        self.N = n + 1
        self.l = [0] * (n + 1)

    # input a, b starts from 1
    def sum(self, a: int, b: int):
        return self.__sum(b) - self.__sum(a - 1)

    # input i starts from 1
    def update(self, i: int, v: int):
        diff = v - self.sum(i, i)
        while i <= N:
            lsb = self.__lsb(i)
            self.l[i] += diff
            i += lsb

    def __lsb(self, i: int):
        return i & -i

    # a starts from 1
    def __sum(self, a):
        if a == 0:
            return 0
        lsb = self.__lsb(a)
        return self.l[a] + self.__sum(a - lsb)

from sys import stdin, stdout

N, M, K = map(int, stdin.readline().split())

tree = FenwickTree(N)
for i in range(1, N + 1):
    x = int(stdin.readline())
    tree.update(i, x)


for _ in range(M + K):
    cmd, a, b = map(int, stdin.readline().split())
    if cmd == 1:
        tree.update(a, b)
    else:
        print(tree.sum(a, b))
