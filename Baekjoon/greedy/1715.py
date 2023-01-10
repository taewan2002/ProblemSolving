import sys
import heapq
input = sys.stdin.readline

# heapq.heappop -> 작은거 순서대로 뽑아옴

card = []
total = 0
N = int(input())
for _ in range(N):
    heapq.heappush(card, int(input()))
    
if len(card) == 1:
    print(0)
else:
    while len(card) > 1:
        tmp = heapq.heappop(card) + heapq.heappop(card)
        total += tmp
        heapq.heappush(card, tmp)
    print(total)