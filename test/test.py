import sys
input = sys.stdin.readline

dp = [0 for _ in range(1000001)]
for i in range(1, 1000001):
    for j in range(i, 1000001, i):
        dp[j] += i
    dp[i] += dp[i-1]
N = int(input())
for _ in range(N):
    print(dp[int(input())])