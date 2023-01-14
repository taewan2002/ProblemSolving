import sys
from collections import deque
import heapq
import pprint
input = sys.stdin.readline

N, K = map(int, input().split())
jew = []
bag = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    heapq.heappush(jew, [tmp[0], -tmp[1]]) # 최대 힙 구현을 위한 음수화
for _ in range(K):
    bag.append(int(input()))
bag.sort() # 작은 가방부터 채운다

tmp = []
total = 0
for i in bag:
    while jew and jew[0][0] <= i: # 보석이 남아있고 가방보다 가볍거나 같은 경우
        heapq.heappush(tmp, heapq.heappop(jew)[1]) # 가격만 푸시
    if tmp:
        total += -(heapq.heappop(tmp)) # 최댓값을 양수로 바꿔서 더해줌
    elif not jew: # 보석이 남지 않은경우
        break
print(total)
