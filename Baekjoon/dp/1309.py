import sys
input = sys.stdin.readline

n = int(input())
dp = [1,3] + [0]*(n-1)
for i in range(2,n+1):
    # [1, 3, 7, 17, 41]
    # n = 2, 사자를 놓지 않는 경우 = (n=1)
    # 사자를 놓는 경우 4 -> 7
    # dp[i] = (dp[i-2]*3 + (dp[i-1]-dp[i-2])*2)
    dp[i] = (dp[i-2] + dp[i-1]*2)%9901
print(dp[-1])