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
    D = [INF for _ in range(N+1)]
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
    return D

for _ in range(int(input())):
    N, M , C = map(int, input().split())
    G = [[]for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        G[b].append([a, c])

    D = dijkstra(C)
    K = 0
    for i in D:
        if i != INF and K < i:
            K = i
    print(len(D)-D.count(INF), K)