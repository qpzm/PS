from sys import stdout
from random import randrange

N = 500_000
MAX =100_000_000
stdout.write(f'{N}\n')
for i in range(N):
    stdout.write(f'{i + 1} ')
