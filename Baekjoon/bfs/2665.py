import sys
from collections import deque
import heapq
# import itertools
# import math
# import bisect
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
INF = sys.maxsize

dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0]

def dijkstra():
    q = []
    heapq.heappush(q, [0, 0, 0])
    V[0][0] = 1
    while q:
        a, x, y = heapq.heappop(q)
        if x == N-1 and y == N-1:
            print(a)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and V[nx][ny] == 0:
                V[nx][ny] = 1
                if G[nx][ny] == 0: # 검은방일때 방을 부시는 횟수 추가
                    heapq.heappush(q, [a+1, nx, ny])
                else:
                    heapq.heappush(q, [a, nx, ny])

N = int(input())
G = []
for _ in range(N):
    G.append(list(map(int, input()[:-1])))
V = [[0 for _ in range(N)] for _ in range(N)]
dijkstra()