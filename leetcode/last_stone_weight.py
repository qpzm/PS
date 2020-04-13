from heapq import heapify, heappop, heappush
from typing import List

def lastStoneWeight(stones: List[int]) -> int:
    stones = [-x for x in stones]
    heapify(stones)
    while(len(stones) > 1):
        x, y = heappop(stones), heappop(stones)
        if x != y:
            heappush(stones, -abs(x - y))

    if stones:
        return -stones[0]
    else:
        return 0

assert(lastStoneWeight([2,7,4,1,8,1]) == 1)
assert(lastStoneWeight([1,1,1,1]) == 0)
