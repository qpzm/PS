n = int(input())
for i in range(1, 2 * n):
    indent = abs(i - n)
    print(' ' * indent + '*' * (n - indent))
