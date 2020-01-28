# Bottom up approach
def count(coins, total, n):
    memo = [1] + [0 for _ in range(total)]

    for j in range(n):
        for i in range(coins[j], total + 1):
            # 왼쪽에서부터 더해가므로 매 순간에는 해당 동전을 한 번 더 사용하는
            # 경우만 계산하지만 해당 동전을 여러 번 사용하는 경우까지 계산됨.
            # e.g. f([1,2,5], 10) = f([1,2], 10) + f([1,2,5], 5)
            memo[i] += memo[i - coins[j]]
    return memo[total]


n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
print(count(coins, k, n))
