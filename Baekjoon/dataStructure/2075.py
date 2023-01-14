import sys
from collections import deque
import heapq
import pprint
input = sys.stdin.readline

N = int(input())
total = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    for i in tmp:
        if len(total) < N:
            heapq.heappush(total, i)
        else:
            if total[0] < i:
                heapq.heappop(total)
                heapq.heappush(total, i)
print(total[0])