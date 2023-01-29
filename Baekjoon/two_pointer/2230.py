import sys
from collections import deque
import heapq
# import itertools
import math
# mport bisect
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
s, e = 0, 1
minNum = INF
while s<len(arr) and e<len(arr):
    if arr[e] - arr[s] >= M:
        minNum = min(minNum, arr[e] - arr[s])
        s += 1
    else:
        e += 1
print(minNum)