from sys import stdin

while True:
    a, b, c = sorted(map(int, stdin.readline().split()))
    if a == b == c == 0: break
    print("right") if a*a + b*b == c*c else print("wrong")
