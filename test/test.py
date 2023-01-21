import sys
# from collections import deque
import heapq
# import itertools
# import math
# import bisect
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    heapq.heappush(heap, [0, start])
    d[start][0] = 0
    while heap:
        cost, cur = heapq.heappop(heap)
        for i, c in w[cur]:
            W = cost + c
            if W < d[i][K-1]:
                d[i][K-1] = W
                d[i].sort()
                heapq.heappush(heap,[W,i])

N, M, K = map(int, input().split())
w = [[] for _ in range(N+1)]
d = [[INF for _ in range(K)]for _ in range(N+1)]
heap = []
for _ in range(M):
    a, b, c = map(int, input().split())
    w[a].append([b, c])

dijkstra(1)

for i in range(1, N+1):
    if d[i][K-1] == INF: # 길이 연결되지 않음
        print(-1)
    else:
        print(d[i][K-1])