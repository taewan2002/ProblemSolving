import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0 for _ in range(K+1)]for _ in range(N+1)]
dp[0][0] = 1

for k in range(N+1):
    for i in range(1, K+1):
        dp[k][i] = dp[k-1][i] + dp[k][i-1]

print(dp[N][K] % 1000000000)