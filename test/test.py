import sys
import pprint
input = sys.stdin.readline

N = int(input())
dp = [[[0, 0] for _ in range(N)] for _ in range(N)]
W = int(input())
wdp = []
for _ in range(W):
    wdp.append(list(map(int, input().split())))

dp[0][0][0] = 0
dp[0][0][1] = 2*N -2
for x in range(N):
    for y in range(N):
        if x == 0 and y == 0:
            continue
        elif x == 0:
            dp[x][y][0] += dp[x][y-1][0] + 1
            dp[x][y][1] += dp[x][y-1][1] - 1
        elif y == 0:
            dp[x][y][0] += dp[x-1][y][0] + 1
            dp[x][y][1] += dp[x-1][y][1] - 1
        else:
            dp[x][y][0] += dp[x-1][y-1][0] + 2
            dp[x][y][1] += dp[x-1][y-1][1] - 2

p1 = []
p2 = []
for i in wdp:
    p1.append(dp[i[0]-1][i[1]-1][0])
    p2.append(dp[i[0]-1][i[1]-1][1])

total = []
tvalue = 0
for i in range(W):
    if p1[i] < p2[i]:
        total.append(1)
        tvalue += p1[i]
    else:
        total.append(2)
        tvalue += p2[i]

print(tvalue)
for i in total:
    print(i)
