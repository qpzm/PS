from collections import deque
from sys import stdin, stdout

q = deque()

def parse(s):
    l = s.split(" ")
    if(len(l) == 1):
        return l[0], None
    else:
        return l[0], l[1]

def process(cmd, item):
    if(cmd == "push"):
        q.append(item)
    elif(cmd == "pop"):
        return q.popleft() if len(q) != 0 else -1
    elif(cmd == "front"):
        return q[0] if len(q) != 0 else -1
    elif(cmd == "back"):
        return q[-1] if len(q) != 0 else -1
    elif(cmd == "size"):
        return len(q)
    elif(cmd == "empty"):
        return int(len(q) == 0)


if __name__ == "__main__":
    N = int(stdin.readline())
    for _ in range(N):
        res = process(*parse(stdin.readline().rstrip()))
        if(res is not None):
            stdout.write(str(res) + '\n')
