from sys import stdin
from itertools import permutations
from math import inf

def calc(costs):
    prev_costs = [0,0,0]
    for i in range(len(costs)):
        prev_costs = _calc(prev_costs, costs[i])
    return prev_costs

def _calc(last_costs, cur_costs):
    costs_by_color = [inf] * 3
    for prev, cur in permutations([0,1,2], 2):
        cost = last_costs[prev] + cur_costs[cur]
        costs_by_color[cur] = min(costs_by_color[cur], cost)
    return(costs_by_color)

def input():
    return stdin.readline().rstrip()

if __name__ == '__main__':
    N = int(input())
    costs = []
    for _ in range(N):
        costs.append(list(map(int, input().split())))
    print(min(calc(costs)))
