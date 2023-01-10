import sys
input = sys.stdin.readline

INF = 10000000
N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]

total = INF
for k in range(3):
    dp = [[INF, INF, INF] for _ in range(N)]
    dp[0][k] = arr[0][k]
    for i in range(1, N):
        for j in range(3):
            dp[i][j] = arr[i][j] + min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])
    for i in range(3):
        if i != k: # 처음, 마지막이 같지 않아야 됨
            total = min(total, dp[-1][i])
print(total)

