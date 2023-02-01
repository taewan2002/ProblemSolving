import sys
from collections import deque
import heapq
import itertools
# import math
# import bisect
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
numList = []
for i in range(1, 11):
    for c in itertools.combinations(range(0, 10), i):
        c = list(c)
        c.sort(reverse=True)
        numList.append(int("".join(map(str, c))))
numList.sort()

try:
    print(numList[N])
except:
    print(-1)
