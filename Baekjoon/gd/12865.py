import sys
from collections import deque
import heapq
import pprint
import itertools
import math
input = sys.stdin.readline


N, K = map(int, input().split())
bag = [[0,0]]
knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]
for _ in range(N):
    bag.append(list(map(int ,input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        w = bag[i][0] # 무게
        v = bag[i][1] # 가치

        if j < w: # 가방 무게보다 w가 무겁다면 새로 넣지 않고 값 가져옴
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(v + knapsack[i-1][j-w], knapsack[i-1][j])
print(knapsack[N][K])