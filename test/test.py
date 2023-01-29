import sys
from collections import deque
import heapq
# import itertools
import math
# mport bisect
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
INF = sys.maxsize

def f(x, y, w):
    h1 = math.sqrt(math.pow(x, 2)-math.pow(w, 2))
    h2 = math.sqrt(math.pow(y, 2)-math.pow(w, 2))
    c = h1*h2/(h1+h2)
    return c

x, y, c = map(float, input().split())
s, e = 0, min(x,y)
total = 0
while e-s > 0.000001:
    mid = (s+e)/2
    if f(x, y, mid) >= c:
        total = mid
        s = mid
    else:
        e = mid
print(f"{total:.3f}")
