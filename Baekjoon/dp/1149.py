import sys
input = sys.stdin.readline

N = int(input())
dp = [list(map(int, input().split()))for _ in range(N)]

for i in range(1, N):
    for j in range(3):
        dp[i][j] += min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])

print(min(dp[-1]))