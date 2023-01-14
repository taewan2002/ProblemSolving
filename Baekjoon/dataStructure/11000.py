import sys
from collections import deque
import heapq
import pprint
input = sys.stdin.readline

N = int(input())
room = []
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort()
heapq.heappush(room, arr[0][1]) # 끝나는 시간만 저장
for i in range(1, N):
    if arr[i][0] < room[0]: # 시작하는 시간이 가장 빨리 끝나는 수업보다 이르면 개설
        heapq.heappush(room, arr[i][1])
    else:
        heapq.heappop(room) # 아니면 그냥 수업 연장? 혹은 끝나고 진행
        heapq.heappush(room, arr[i][0])
print(len(room))
