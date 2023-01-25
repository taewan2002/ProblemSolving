import sys
from collections import deque
import heapq
# import itertools
# import math
# import bisect
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(s):
    D = [INF for _ in range(N+1)]
    q = []
    heapq.heappush(q, [0, s])
    D[s] = 0

    while q:
        d, now = heapq.heappop(q)
        if d > D[now]:
            continue
        for v, w in G[now]:
            cost = w + d
            if cost < D[v]:
                D[v] = cost
                heapq.heappush(q, [cost, v])
    return D

N, M, X = map(int, input().split())
G = [[]for _ in range(N+1)for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a].append([b, c])
    # G[b].append([a, c])

total = 0
for i in range(1, N+1):
    go = dijkstra(i)
    back = dijkstra(X)
    total = max(total, go[X]+back[i])

print(total)