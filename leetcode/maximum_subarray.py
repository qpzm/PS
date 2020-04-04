def maxSubArray(nums):
    best, sum = nums[0], nums[0]
    for i in range(1, len(nums)):
        n = nums[i]
        sum = max(n, sum + n)
        best = max(best, sum)
    return best

assert(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) ==  6)
assert(maxSubArray([-2,-1,-3,-4,-1,-2,-1,-5,-4]) == -1)
