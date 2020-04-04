def moveZeroes(nums):
    N, i = len(nums), 0
    while(i < N):
        if nums[i] == 0:
            nums.append(nums.pop(i))
            N -= 1
        else:
            i += 1
    return nums

assert(moveZeroes([0,1,0,3,12]) == [1,3,12,0,0])
assert(moveZeroes([0]) == [0])
assert(moveZeroes([1]) == [1])
assert(moveZeroes([0,0,1]) == [1,0,0])
