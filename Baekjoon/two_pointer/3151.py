import sys
from collections import deque
import heapq
# import itertools
# import math
# import bisect
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
total = 0

# 한 개의 수 선택 후 투포인터 돌리기
for i in range(N-2):
    l, r = i+1, N-1
    goal = -arr[i]
    mxidx = N
    while l < r:
        tmp = arr[l] + arr[r]
        if tmp < goal:
            l += 1
        elif tmp == goal:
            if arr[l] == arr[r]:
                total += r - l
            else:
                if mxidx > r:
                    mxidx = r
                    while mxidx >= 0 and arr[mxidx-1] == arr[r]:
                        mxidx -= 1
                total += r - mxidx + 1
            l += 1
        else:
            r -= 1
print(total)