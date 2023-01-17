import sys
from collections import deque
import heapq
import itertools
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 1 3 6 6 7 9
N = int(input())
K = int(input())
arr = list(map(int, input().split()))
arr.sort()

if K >= N:
    print(0)
else:
    dist = []
    for i in range(1, N):
        dist.append(arr[i]-arr[i-1])

    for _ in range(K-1):
        dist[dist.index(max(dist))] = 0
    print(sum(dist))