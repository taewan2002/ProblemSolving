import sys
from collections import deque
import heapq
import pprint
import itertools
input = sys.stdin.readline

N = int(input())
room = []
for _ in range(N):
    room.append(list(map(int, input().split())))

room.sort(key=lambda x: x[1])
mroom = []
heapq.heappush(mroom, room[0][2])

for i in range(1, N):
    if room[i][1] < mroom[0]:
        heapq.heappush(mroom, room[i][2])
    else:
        heapq.heappop(mroom)
        heapq.heappush(mroom, room[i][2])
print(len(mroom))