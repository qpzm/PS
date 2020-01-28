import sys

MAX_SIZE = 100000
def main():
    i = 0
    result = 0
    heap = Heap(lambda x,y: x-y)

    for _ in range(int(sys.stdin.readline())):
        command = int(sys.stdin.readline())
        if(command == 0):
            print(heap.pop())
        else:
            heap.push(command)
        i += 1

class Heap:
    # If a return value from comparator is positive, x goes closer to the root
    # Default: MinHeap
    def __init__(self, comparator = lambda x,y: y-x):
        self.list = [0] * MAX_SIZE
        self.size = 0
        self.comparator = comparator

    def push(self, item):
        self.list[self.size] = item
        self.bubble_up(self.size)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return 0

        result = self.list[0]
        self.list[0] = self.list[self.size - 1]
        self.size -= 1
        self.bubble_down(0)
        return result

    def bubble_up(self, curr):
        if curr == 0:
            return
        parent = (curr - 1) // 2
        if self.comparator(self.list[curr], self.list[parent]) >= 0:
            self.__swap(curr, parent)
            self.bubble_up(parent)

    def bubble_down(self, curr):
        higher = curr
        left_child = 2*curr + 1
        if left_child <= self.size - 1:
            if self.comparator(self.list[higher], self.list[left_child]) < 0:
                higher = left_child

        right_child = 2*curr + 2
        if right_child <= self.size - 1:
            if self.comparator(self.list[higher], self.list[right_child]) < 0:
                higher = right_child

        if higher != curr:
            self.__swap(curr, higher)
            self.bubble_down(higher)

    def __swap(self, x, y):
        tmp = self.list[x]
        self.list[x] = self.list[y]
        self.list[y] = tmp

if __name__ == "__main__":
    main()
