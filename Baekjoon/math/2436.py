import sys
import math
input = sys.stdin.readline

N, M  = map(int, input().split())

NM = N*M
total = []
for i in range(N, M+1, N):
    tmp = NM//i
    if i > tmp:
        break
    elif math.gcd(i, tmp) == N and math.lcm(i, tmp) == M:
        total.append([i, tmp])
print(*total[-1])