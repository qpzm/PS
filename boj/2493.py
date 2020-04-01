from sys import stdin, stdout

MAX_HEIGHT = 100_000_000

def find(left_towers, tower, loc):
    for i in range(loc - 1, -1, -1):
        if left_towers[i] >= tower:
            return i

N = int(stdin.readline().rstrip())
towers = [MAX_HEIGHT] + list(map(int, stdin.readline().rstrip().split()))
for loc, tower in enumerate(towers[1:], start=1):
    stdout.write(f'{find(towers, tower, loc)} ')
