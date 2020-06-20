import sys


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def same_set(self, x, y, format=lambda x: x):
        if self.find(x) == self.find(y):
            return format(True)
        else:
            return format(False)

    def find(self, x):
        y = x
        while(y != self.parent[y]):
            y = self.parent[y]

        self.parent[x] = y
        return y

    def union(self, x, y):
        p_x, p_y = self.parent[x], self.parent[y]

        # Ensure self.size[p_x] >= self.size[p_y]
        if(self.size[p_x] < self.size[p_y]):
            p_x, p_y = p_y, p_x

        self.parent[p_y] = p_x
        self.size[p_x] += self.size[p_y]


def format(bool):
    if bool:
        return 'YES'
    else:
        return 'NO'


def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    u = UnionFind(N + 1)
    for _ in range(M):
        cmd, x, y = map(int, sys.stdin.readline().rstrip().split())
        if cmd == 0:
            u.union(x, y)
        else:
            sys.stdout.write(u.same_set(x, y, format))
            sys.stdout.write('\n')


if __name__ == '__main__':
    main()
