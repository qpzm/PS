from sys import stdin, stdout
input = stdin.readline
print = lambda x: stdout.write(x + '\n')

def sol(s):
    num_left = 0
    for c in s:
        if c == '(':
            num_left += 1
        else:
            num_left -= 1
            if num_left < 0:
                break

    return num_left == 0

for _ in range(int(input())):
    if sol(input().rstrip()):
        print('YES')
    else:
        print('NO')
