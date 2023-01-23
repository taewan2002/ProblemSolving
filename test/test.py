import sys
from collections import deque
import heapq
# import itertools
# import math
# import bisect
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
arr = [int(input()) for _ in range(N)]
sumList = [arr[0]]

for i in range(len(arr)-1):
    sumList.append(max(sumList[i] + arr[i+1], arr[i+1]))
print(max(sumList))
