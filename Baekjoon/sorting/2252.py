import sys
from collections import deque
import heapq
import itertools
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# 위상 정렬

N, M = map(int, input().split())

g = [[] for _ in range(N+1)]
d = [0 for _ in range(N+1)]
q = deque()
total = []

for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    d[b] += 1

for i in range(1, N+1):
    if d[i] == 0: # 선행 조건이 없는 수, 2가 3보다 앞에 있어야 한다 일때 2
        q.append(i)

while q:
    tmp = q.popleft()
    total.append(tmp)
    for i in g[tmp]:
        d[i] -= 1
        if d[i] == 0:
            q.append(i)
print(*total)