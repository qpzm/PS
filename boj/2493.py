from sys import stdin, stdout

def find(stack, tower, loc):
    while len(stack) != 0:
        left_height, left_loc = stack[-1]
        if  left_height < tower:
            stack.pop()
        else:
            stack.append((tower, loc))
            return left_loc

    stack.append((tower, loc))
    return 0

N = int(stdin.readline().rstrip())
stack = []
towers = list(map(int, stdin.readline().rstrip().split()))
for loc, tower in enumerate(towers, start=1):
    stdout.write(f'{find(stack, tower, loc)} ')
