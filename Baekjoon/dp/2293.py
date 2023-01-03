import sys
input = sys.stdin.readline

N, K = map(int, input().split())
s = [int(input()) for _ in range(N)]
dp = [0 for _ in range(K+1)]
dp[0] = 1

for i in s:
    for k in range(i, K+1):
        dp[k] += dp[k-i]

print(dp[-1])