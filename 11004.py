import random


def find_kth(l, k):
    pivot = l.pop(random.randrange(len(l)))
    left, right = [], []
    left_length = 0
    for n in l:
        if n > pivot:
            right.append(n)
        else:
            left.append(n)
            left_length += 1

    if k <= left_length:
        return find_kth(left, k)
    elif k == (left_length + 1):
        return pivot
    else:
        return find_kth(right, k - left_length - 1)


N, K = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]
print(find_kth(nums, K))
