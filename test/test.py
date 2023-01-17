import sys
from collections import deque
import heapq
import itertools
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

v = list(map(int, input().split()))
left = []
right = []
for i in v:
    if i < 0:
        left.append(i)
    elif i > 0:
        right.append(i)

dist = []
left.sort()
right.sort(reverse=True)
for i in range(len(left)//M): # M개씩 이동
    dist.append(abs(left[M*i])) # M개중 더 큰 cost 추가
if len(left) % M > 0: # 남는거 만큼 cost 추가
    dist.append(abs(left[(len(left)//M)*M]))

for i in range(len(right)//M): # M개씩 이동
    dist.append(abs(right[M*i]))
if len(right) % M > 0:
    dist.append(abs(right[(len(right)//M)*M]))

print(sorted(v))
               
print(dist)
dist.sort()
tmp = dist.pop()
tmp += 2*sum(dist)
print(tmp) # 가장 비싼건 마지막에, 나머지는 먼저 갔다온다.