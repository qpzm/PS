# 왜 채점 서버에서만 런타임에러?
N = int(input())
nums = [int(x) for x in input().split()]
sums = [nums[0]]
for i in range(1, N):
    prev_sum = max([sums[j] for j in range(i) if nums[j] < nums[i]])
    sums.append(prev_sum + nums[i])
print(max(sums))
