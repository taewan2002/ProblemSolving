import sys
from collections import deque
import heapq
import itertools
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

v = []
people = 0
for _ in range(N):
    v.append(list(map(int, input().split())))
    people += v[-1][1]

v.sort(key=lambda x: x[0])
p = 0
for i in range(N):
    p += v[i][1]
    if p >= people//2:
        print(v[i][0])
        break