from sys import stdin, stdout

def push(item):
    q.append(item)
    return item

def pop():
    if empty():
        return -1
    else:
        return q.pop(0)

def front():
    if empty():
        return -1
    else:
        return q[0]

def back():
    if empty():
        return -1
    else:
        return q[len(q) - 1]

def size():
    return len(q)

def empty():
    return int(len(q) == 0)

q = []
N = int(stdin.readline())
i = 0
switcher = {
    'push': push,
    'pop': pop,
    'size': size,
    'front': front,
    'back': back,
    'empty': empty
}

while(i < N):
    command = stdin.readline().split()
    if(len(command) == 1):
        operator = command[0]
        result = switcher[operator]()
    elif(len(command) == 2):
        operator, operand = command[0], int(command[1])
        result = switcher[operator](operand)
    else:
        raise Exception

    if(operator != 'push'):
        stdout.write(str(result) + '\n')
    i += 1
