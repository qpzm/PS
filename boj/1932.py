from sys import stdin

N = int(stdin.readline())
nums = []
for _ in range(N):
    nums.append(list(map(int, stdin.readline().strip().split())))

prev_max = [nums[0][0]]
for i in range(1, len(nums)):
    cur_max = []
    row_len = len(nums[i])
    for j in range(row_len):
        if j == 0:
            selection = prev_max[j]
        elif j == row_len - 1:
            selection = prev_max[j-1]
        else:
            selection = max(prev_max[j-1], prev_max[j])
        cur_max.append(nums[i][j] + selection)
    prev_max = cur_max

print(max(prev_max))
