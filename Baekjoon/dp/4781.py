import sys
from collections import deque
import heapq
import pprint
import itertools
import math
input = sys.stdin.readline

while True:
    n, m = map(float, input().split())
    n, m = int(n), int(m*100 +0.5) # 부동 소숫점 오류
    if n == 0:
        break
    dp = [0 for _ in range(m+1)]
    for _ in range(n):
        c, p = (map(float, input().split()))
        c, p = int(c), int(p*100+0.5)

        for i in range(p, m+1):
            dp[i] = max(dp[i], dp[i-p] + c)
    print(dp[m]) 
