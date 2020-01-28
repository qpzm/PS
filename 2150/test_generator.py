import random

# n = random.randint(1,10000)
# m = random.randint(1,10000)
n, m = 10000, 50000
print(n, m)
for _ in range(m):
    print(' '.join(map(str, random.sample(range(1, n), 2))))
