import sys
from collections import deque
import heapq
# import itertools
# import math
# import bisect
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
INF = sys.maxsize

def M():
    sheap = []
    bheap = []
    middle = arr[0]
    total = [middle]
    for idx, val in enumerate(arr[1:], 1):
        if val > middle: # 변수가 중앙값 보다 크면
            heapq.heappush(bheap, val) # 최소힙
        else: # 변수가 중앙값 보다 작으면
            heapq.heappush(sheap, -val) # 최대힙
        
        if idx % 2 == 0: # 홀수 번 째 마다
            if len(sheap) < len(bheap): # 최소 힙의 갯수가 많으면
                heapq.heappush(sheap, -middle) # 최대 힙에 푸시하고
                middle = heapq.heappop(bheap) # 최소힙에서 중앙값 가져오기
            elif len(sheap) > len(bheap):
                heapq.heappush(bheap, middle)
                middle = -heapq.heappop(sheap)
            total.append(middle)

    print(len(total))
    for i in range(len(total)):
        if i != 0 and (i+1)%10 == 1:
            print()
        print(total[i], end=" ")
    print()

for i in range(int(input())):
    N = int(input())
    arr = []
    if N % 10 == 0:
        for _ in range(N//10):
            arr.extend(list(map(int, input().split())))
    else:
        for _ in range(N//10+1):
            arr.extend(list(map(int, input().split())))
    M()