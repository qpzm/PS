class NumArray:
    # MAX_LEN = 3 * 10 ** 4
    MAX_LEN = 2 ** 15
    # e.g. if 2 is MAX_LEN, 3 is MAX_INDEX
    MAX_INDEX = 2 * MAX_LEN - 1

    def __init__(self, nums: list[int]):
        self.nums = [0] * (2 * NumArray.MAX_LEN)
        for (i, n) in enumerate(nums):
            self.update(i, n)

    def update(self, index: int, val: int) -> None:
        j = NumArray.MAX_LEN + index
        original = self.nums[j]
        diff = val - original
        while j != 0:
            self.nums[j] += diff
            j //= 2

        self.nums[0] += diff

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        left_index = NumArray.MAX_LEN + left
        right_index = NumArray.MAX_LEN + right

        while left_index != right_index and left_index < right_index:
            if left_index % 2 == 1:
                res += self.nums[left_index]
                left_index += 1

            if right_index % 2 == 0:
                res += self.nums[right_index]
                right_index -= 1

            left_index //= 2
            right_index //= 2

        if left_index == right_index:
            res += self.nums[left_index]

        return res
