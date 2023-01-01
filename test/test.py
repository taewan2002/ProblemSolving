import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    if i == 0:
        continue
    for k in range(M):
        if dp[i][k] == 0:
            continue
        if k == 0:
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
        elif k == M-1:
            dp[i][-1] = dp[i-1][-1] + dp[i-1][-2]
        else:
            dp[i][k] = dp[i-1][k-1] + dp[i-1][k] + dp[i-1][k+1]

print(sum(dp[N-1])%1000000007)