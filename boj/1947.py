def solve(n):
    if n == 1: return 0
    a, b = 0, 1
    for i in range(2, n):
        a, b= b, (a + b) * i % 1_000_000_000
    return b

print(solve(int(input())))
assert(solve(1) == 0)
assert(solve(2) == 1)
assert(solve(3) == 2)
assert(solve(4) == 9)
assert(solve(5) == 44)
