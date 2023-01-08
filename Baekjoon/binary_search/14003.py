import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(N)] # 역추적을 위한 dp
lis = []
l = 0
for i in range(N):
    n = arr[i]
    idx = bisect_left(lis, n)
    
    if idx == l:
        lis.append(n)
        l += 1
    else:
        lis[idx] = n
    dp[i] = idx # dp에 저장
print(l)
toPrint = [] # 역추적
for i in range(N-1, -1, -1):
    if dp[i] == l-1:
        toPrint.append(arr[i])
        l -= 1
print(*reversed(toPrint))