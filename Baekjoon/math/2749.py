# 분할정복

n = int(input())

dp = []
dp.append(0) #dp[0] = 0
dp.append(1) #dp[1] = 1

m = 10 ** 6
p = 15 * (m//10)

for i in range(2, p):
    dp.append((dp[i-1] + dp[i-2]) % m)
    print(dp)
    print()
        
print(dp[n%p])