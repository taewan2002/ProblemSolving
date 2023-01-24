import sys
from collections import deque
import heapq
# import itertools
# import math
# import bisect
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    D[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if D[now] < d:
            continue
        for v, w in G[now]:
            cost = d + w
            if cost < D[v]:
                D[v] = cost
                heapq.heappush(q, [cost, v])

N, M = map(int, input().split())
s = int(input())
G = [[]for _ in range(N+1)]
D = [INF for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a].append([b, c])

dijkstra(s)

for i in range(1, N+1):
    print("INF" if D[i] == INF else D[i])