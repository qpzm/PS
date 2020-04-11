from math import inf

# Memoize current min every stack entry
class MinStack:
    def __init__(self):
        self.stk = []

    def push(self, x: int) -> None:
        cur_min = min(self.getMin(), x)
        self.stk.append((x, cur_min))

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        if self.stk:
            return self.stk[-1][1]
        else:
            return inf

stk = MinStack()
stk.push(-2)
stk.push(0)
stk.push(-3)
assert(-3 == stk.getMin())
stk.pop()
assert(0 == stk.top())
assert(-2 == stk.getMin())
