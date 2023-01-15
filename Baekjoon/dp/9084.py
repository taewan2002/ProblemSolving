import sys
from collections import deque
import heapq
import pprint
import itertools
import math
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    coin = list(map(int, input().split()))
    total = int(input())
    dp = [0 for _ in range(total+1)]
    dp[0] = 1
    for c in coin:
        for i in range(total+1):
            if c <= i:
                dp[i] += dp[i-c]
    print(dp[total])