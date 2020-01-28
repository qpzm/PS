# O(n^2) solution
N = int(input())
nums = [int(x) for x in input().split()]
sums = [nums[0]]
for i in range(1, N):
    max_before = 0
    for j in range(i):
        if nums[j] < nums[i] and max_before < sums[j]:
            max_before = sums[j]
    sums.append(max_before + nums[i])
print(max(sums))
