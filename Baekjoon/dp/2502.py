import sys
input = sys.stdin.readline

D, K = map(int, input().split())
dp = [0 for _ in range(D)]

while dp[-1] != K:
    dp[0] += 1
    dp[1] = dp[0]
    dp[-1] = 0
    while dp[-1] < K:
        for i in range(2, D):
            dp[i] = dp[i-1] + dp[i-2]
        if dp[-1] == K:
            break
        dp[1] += 1

print(dp[0])
print(dp[1])