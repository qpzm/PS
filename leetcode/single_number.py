from functools import reduce

# xor is commutative and x ^ x = 0
def singleNumber(nums):
    return reduce(lambda x, y: x ^ y, nums)
