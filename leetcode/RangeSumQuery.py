class NumArray:
    # MAX_LEN = 3 * 10 ** 4
    MAX_LEN = 2 ** 15
    # e.g. if 2 is MAX_LEN, 3 is MAX_INDEX
    MAX_INDEX = 2 * MAX_LEN - 1

    def __init__(self, nums: list[int]):
        self.nums = [0] * (2 * NumArray.MAX_LEN)

        def build(i, left, right):
            if left == right:
                if left <= len(nums) - 1:
                    self.nums[i] = nums[left]
                    return self.nums[i]
                else:
                    return 0

            mid = left + (right - left) // 2
            self.nums[i] = build(i * 2, left, mid) + build(i * 2 + 1, mid + 1, right)
            return self.nums[i]

        print(build(1, 0, NumArray.MAX_LEN - 1))

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

        while left_index < right_index:
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

cmds = ["NumArray", "sumRange","sumRange","sumRange","update","update","update","sumRange","update","sumRange","update"]
args = [[[0,9,5,7,3]],[4,4],[2,4],[3,3],[4,5],[1,7],[0,8],[1,2]]
for (c, arg) in zip(cmds, args):
    if c == "NumArray":
        print(arg)
        obj = NumArray(*arg)
    if c == "sumRange":
        print("sumRange", *arg, obj.sumRange(*arg))
    elif c == "update":
        obj.update(*arg)
