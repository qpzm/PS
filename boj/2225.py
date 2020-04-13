from math import comb

def solve(n, k):
    dp = [1] * (n+1)
    for _ in range(k-1):
        for i in range(1, n+1):
            dp[i] = (dp[i] + dp[i-1]) % 1_000_000_000
    return dp[n]

def solve2(n, k):
    return(comb(n+k-1, k-1) % 1_000_000_000)

# N, K = map(int, input().split())
# print(solve(N, K))

tests = [(20, 2), (20, 3), (200, 200)]
for n, k in tests:
    assert(solve(n,k) == solve2(n,k))
