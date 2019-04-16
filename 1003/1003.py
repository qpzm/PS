import sys

def main():
    N = int(input())
    memo = {0: (1, 0), 1: (0, 1)}
    for _ in range(N):
        n = int(sys.stdin.readline())
        print("%d %d" % count_fib(n, memo))


def count_fib(n, memo):
    if n not in memo:
        memo[n] = tuple([sum(x) for x in zip(
            count_fib(n - 1, memo), count_fib(n - 2, memo))])
    return memo[n]


if __name__ == "__main__":
    main()
