import sys
from collections import deque
import heapq
import pprint
input = sys.stdin.readline

K, N  = map(int, input().split())
p = list(map(int, input().split()))
total = []

for i in p:
    heapq.heappush(total, i)

minNum = 0
for _ in range(N):
    minNum = heapq.heappop(total) # 큐에서 작은 순서대로 뽑아짐
    for i in p:
        tmp = minNum * i # 지금 큐에 들어있는 가장 작은 수랑 곱한것을 다시 추가
        heapq.heappush(total, tmp)

        if minNum % i == 0: # 5 * 2, 2 * 5 와 같은 중복 방지 한번 겹치는 순간 그 반복문에서 발생하는 수는 중복
            break
print(minNum) # N번 째 최솟값

# 2 5 7
# 2 4 5
