import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    K = int(input())
    dp = []
    for _ in range(2):
        dp.append(list(map(int, input().split())))
    for k in range(1, K):
        if k == 1:
            dp[0][k] += dp[1][k-1]
            dp[1][k] += dp[0][k-1]
        else:
            dp[0][k] += max(dp[1][k-1], dp[1][k-2])
            dp[1][k] += max(dp[0][k-1], dp[0][k-2])
    print(max(dp[0][-1], dp[1][-1]))

