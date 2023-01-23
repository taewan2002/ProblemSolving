import sys
from collections import deque
import heapq
# import itertools
# import math
# import bisect
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
graph  = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# 트리생성
for _ in range(n - 1):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

# [내가 ea가 아닐 때 ea의 수, 내가 ea일때 ea의 수]
dp = [[0, 1] for _ in range(n + 1)]

def solve_dp(num):
  visited[num] = True

  for i in graph[num]:
    if not visited[i]:
      solve_dp(i) # 아직 방문하지 않은 곳을 탐색
      dp[num][0] += dp[i][1] # child가 무조건 ea어야 함
      dp[num][1] += min(dp[i][0], dp[i][1]) # ea여부와 상관없이 더 작은 값을 가져옴

solve_dp(n-1)
print(min(dp[n-1][0], dp[n-1][1]))