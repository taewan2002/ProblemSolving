import sys
from collections import deque
import heapq
import itertools
import math
import bisect
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(px, py, d, s):
    global total
    if d == K:
        total = max(total, s)
        return
    for x in range(px, N):
        for y in range(py if x==px else 0, M):
            if v[x][y]:
                continue

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and v[nx][ny]:
                    break
            else:
                v[x][y] = True
                dfs(x, y, d+1, s+arr[x][y])
                v[x][y] = False

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[False for _ in range(M)]for _ in range(N)]

q = []
total = -1000000
dfs(0, 0, 0, 0)
print(total)