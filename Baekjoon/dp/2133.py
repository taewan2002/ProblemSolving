import sys
from collections import deque
import heapq
# import itertools
# import math
# import bisect
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
dp = [0 for _ in range(31)]
dp[2] = 3
for i in range(4, N+1, 2):
    dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2
print(dp[N])
# 3 * 2 ->  3
# 3 * 4 -> 9 + 2