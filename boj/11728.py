from sys import stdin, stdout
parse = lambda: map(int, stdin.readline().split())
M, N = parse()
l1, l2 = list(parse()), list(parse())
l1.sort(reverse=True)
l2.sort(reverse=True)

while(not(M == 0 and N == 0)):
    if M == 0:
        while(N != 0):
            stdout.write(f'{l2.pop()} ')
            N -= 1
    elif N == 0:
        while(M != 0):
            stdout.write(f'{l1.pop()} ')
            M -= 1
    elif l1[-1] < l2[-1]:
        stdout.write(f'{l1.pop()} ')
        M -= 1
    else:
        stdout.write(f'{l2.pop()} ')
        N -= 1
