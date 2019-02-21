MAX_SIZE = 10000

def main():
    N = int(input())
    i = 0
    result = 0
    queue = Queue()

    while(i < N):
        command = input().split()
        if(len(command) == 1):
            operator = command[0]
            result = getattr(queue, operator)()
        elif(len(command) == 2):
            operator = command[0]
            operand = int(command[1])
            result = getattr(queue, operator)(operand)
        else:
            raise Exception

        if(operator != 'push'):
            print(result)
        i += 1

class Queue:
    """
    Problem Current Impl: start, end only increasing what if exceeds int range?
    """
    def __init__(self):
        self.q = [None] * MAX_SIZE
        self.start = 0
        self.end = 0
        self.max_size = MAX_SIZE

    def push(self, item):
        self.end += 1
        self.q[self.end % self.max_size - 1] = item
        return item

    def pop(self):
        if self.empty():
            return -1
        else:
            item = self.q[self.start % self.max_size]
            self.start += 1
            return item

    def front(self):
        if self.empty():
            return -1
        else:
            return self.q[self.start % self.max_size]

    def back(self):
        if self.empty():
            return -1
        else:
            return self.q[self.end % self.max_size - 1]

    def size(self):
        return self.end - self.start

    def empty(self):
        return int(self.size() == 0)

if __name__ == "__main__":
    main()
