# Failed: Too much memory
def count(total, coins, memo, n):
    if(n == 1):
        return 1
    elif (n, total) in memo:
        return memo[(n, total)]
    else:
        memo[(n, total)] = sum(map(lambda i: count(total - i * coins[-1], coins[:-1], memo, n - 1),
                        range(0, total // coins[-1] + 1)))
        return memo[(n, total)]


n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
print(count(k, coins, {}, n))
