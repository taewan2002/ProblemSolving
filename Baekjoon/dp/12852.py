import sys
from collections import deque
import heapq
import itertools
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
dp = [[0, []] for _ in range(n + 1)]
dp[1][0] = 0
dp[1][1] = [1]

for i in range(2, n+1):
    dp[i][0] = dp[i-1][0] + 1 # 1더하기
    dp[i][1] = dp[i-1][1] + [i] # 배열에 숫자 추가하기
    if i % 3 == 0 and dp[i//3][0] + 1 < dp[i-1][0]: # 길이를 더 짧게 만들 수 있다면
        dp[i][0] = dp[i//3][0] + 1
        dp[i][1] = dp[i//3][1] + [i]
    if i % 2 == 0 and dp[i // 2][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 2][0] + 1
        dp[i][1] = dp[i // 2][1] + [i]

print(dp[n][0])
print(*reversed(dp[n][1]))