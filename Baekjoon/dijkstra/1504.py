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

N, E = map(int, input().split())
G = [[]for _ in range(N+1)for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    G[a].append([b, c])
    G[b].append([a, c])
v1, v2 = map(int, input().split())

one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
cnt = min(one[v1] + v1_[v2] + v2_[N], one[v2] + v2_[v1] + v1_[N])
print(cnt if cnt < INF else -1)