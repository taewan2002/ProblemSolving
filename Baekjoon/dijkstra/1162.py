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
    q = []
    cnt = 0
    D[s][cnt] = 0
    heapq.heappush(q, [0, s, cnt])

    while q:
        cW, now, cnt = heapq.heappop(q)
        if D[now][cnt] < cW:
            continue
        for next, w in G[now]:
            next_W = w + cW
            if D[next][cnt] > next_W:
                D[next][cnt] = next_W
                heapq.heappush(q, [next_W, next, cnt])
            
            # 도로 포장 횟수가 남았고, 더 작은 가중치를 넣어줌
            if cnt < K and D[next][cnt+1] > cW:
                D[next][cnt+1] = cW
                heapq.heappush(q, [cW, next, cnt+1])

N, M, K = map(int, input().split())
G = [[] for _ in range(N+1)]
D = [[INF for _ in range(K+1)] for _ in range(N+1)] # 도로 포장 갯수 확인
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a].append([b, c])
    G[b].append([a, c])

dijkstra(1)
print(min(D[N]))