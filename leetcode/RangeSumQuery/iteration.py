# https://leetcode.com/problems/range-sum-query-mutable/
# TODO
# 1. Use only 2N + 1
# 2. build with for loop
class NumArray:
    # The root starts from index 1
    #      1
    #   2    3
    # 4  5 6
    def __init__(self, nums: list[int]):
        self.n = len(nums)
        n = self.n
        self.tree = [0] * (2 * n + 1)  # total 0, 1 ~ 7

        for i in range(0, n):
            # use index from 1
            # non-leaf: 1 ~ n - 1,  count: n - 1
            # leaf:     n ~ 2n - 1, count: n
            #     e.g. last: 2n - 1 - n = n - 1
            # i starts from 0, leaf starts from n + 1 (when 0 is not used)
            self.tree[i + n + 1] = nums[i]

        def get_tree(index):
            m = len(self.tree)
            if index >= m:
                return 0
            else:
                return self.tree[index]

        for i in range(n, 0, -1):
            self.tree[i] = get_tree(2 * i) + get_tree(2 * i + 1)

        # print(self.tree)

    def update(self, index: int, val: int) -> None:
        j = self.n + index + 1
        original = self.tree[j]
        diff = val - original
        while j != 0:
            self.tree[j] += diff
            j //= 2

        # print(self.tree)

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        left_index = self.n + left + 1
        right_index = self.n + right + 1

        while left_index <= right_index:
            if left_index % 2 == 1:
                res += self.tree[left_index]
                left_index += 1

            if right_index % 2 == 0:
                res += self.tree[right_index]
                right_index -= 1

            left_index //= 2
            right_index //= 2

        return res

cmds = ["NumArray","sumRange","update","sumRange"]
args = [[[1,3,5]],[0,2],[1,2],[0,2]]

for (c, arg) in zip(cmds, args):
    if c == "NumArray":
        print(arg)
        obj = NumArray(*arg)
    if c == "sumRange":
        print("sumRange", *arg, obj.sumRange(*arg))
    elif c == "update":
        obj.update(*arg)
