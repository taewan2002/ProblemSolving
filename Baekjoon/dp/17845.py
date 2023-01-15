import sys
from collections import deque
import heapq
import pprint
import itertools
import math
input = sys.stdin.readline

N, K = map(int, input().split())

gpa = [[0,0]]
for _ in range(K):
    gpa.append(list(map(int, input().split())))

dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
for i in range(1, K+1):
    for j in range(1, N+1):
        t = gpa[i][1] # 공부시간
        g = gpa[i][0] # 중요도

        if j < t:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-t] + g)

print(dp[K][N])