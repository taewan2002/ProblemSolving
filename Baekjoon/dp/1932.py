import sys
input = sys.stdin.readline

N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    if i == 0:
        continue
    for k in range(i+1):
        if k == 0:
            dp[i][0] += dp[i-1][0]
        elif k == i:
            dp[i][-1] += dp[i-1][-1]
        else:
            dp[i][k] += max(dp[i-1][k-1], dp[i-1][k])

print(max(dp[N-1]))