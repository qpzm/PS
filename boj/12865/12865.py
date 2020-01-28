N, K = map(int, input().split())
items = []
# weight: 0 to K
memo = [[None for _ in range(K + 1)] for _ in range(N)]
for _ in range(N):
    items.append(map(int, input().split()))

for i in range(N):
    w, v = items[i]
    for j in range(K + 1):
        if j == 0:
            memo[i][j] = 0
        elif w > j:
            memo[i][j] = memo[i-1][j] if i else 0
        else:
            memo[i][j] = max(memo[i-1][j], v + memo[i-1][j-w]) if i else v

print(memo)
print(memo[i][j])
