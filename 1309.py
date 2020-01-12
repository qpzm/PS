# 맨 아래가 xx로 끝나면 밑에 xo xx ox 3 가지가 붙을 수 있으므로 3 * 2f(i-2)
# xo 또는 ox로 끝나면 밑에 ox 혹은xo 중 하나, xx가 붙을 수 있어서 2 * (f(i-1) - f(i-2))
# 따라서 f(i) = f(i-2) + 2f(i-1)
n = int(input())
a, b = 1, 3
for _ in range(2, n + 1):
    a, b = b, a + 2 * b
print(b % 9901)
