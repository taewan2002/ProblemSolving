import sys
from collections import deque
import heapq
import pprint
import itertools
import math
input = sys.stdin.readline

N, M = map(int, input().split())
active = list(map(int, input().split()))
inactive = list(map(int ,input().split()))
# 메모리 초과 발생 방지, 만들 수 있는 최대값 까지만 배열 생성
dp = [[0 for _ in range(sum(inactive)+1)]for _ in range(N+1)]
total = sum(inactive)
for i in range(1, N+1):
    b = active[i-1]
    c = inactive[i-1]

    for j in range(1, sum(inactive)+1):
        if j < c:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c] + b)
        
        if dp[i][j] >= M: # 조건 만족일 때 최소 코스트 갱신
            total = min(total, j)

print(total)
#print(dp)

# 10 30 20 35 40
# 0  3  3  4  5