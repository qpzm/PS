from itertools import product
from lock_and_key_before import solution as sol1
from lock_and_key import solution as sol2

M, N = map(int, input().split())

def to_matrix(l, n):
    return [l[i * n :(i+1) * n] for i in range(n)]

def gen_key_lock(M, N):
    keys = product([0, 1], repeat= M ** 2)
    locks = product([0, 1], repeat= N ** 2)

    for key_1d, lock_1d in product(keys, locks):
        key, lock = to_matrix(key_1d, M), to_matrix(lock_1d, N)
        yield key, lock

cnt = 0
for key, lock in gen_key_lock(M, N):
    res1, res2 = sol1(key, lock), sol2(key, lock)
    if  res1 != res2:
        print(key, lock)
        print(res1, res2)
        break
    else:
        print(cnt)
        cnt += 1
