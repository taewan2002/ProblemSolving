import sys
from collections import deque
import heapq
import itertools
import math
import bisect
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def get_max(node):
    global total_list
    global cnt
    lb = bisect.bisect_left(total_list, node)
    if lb > 0:
        left = high[total_list[lb - 1]]
    else:
        left = 0
    if lb < len(total_list):
        right = high[total_list[lb]]
    else:
        right = 0
    high[node] = max(left, right) + 1
    cnt +=  max(left, right) + 1
    total_list.insert(lb, node)

    return high[node]

n = int(input())
total = 0
total_list = []
cnt = 0
high = [0] * (n + 1)
tmp = int(input())
total_list.append(tmp)
print(cnt)
for i in range(1, n):
    total += get_max(int(input()))
    print(cnt)