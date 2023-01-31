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

A = []
A_dict = {}
numList = []

for _ in range(N):
    A.append(input().rstrip())

for i in range(N):
    for j in range(len(A[i])):
        if A[i][j] in A_dict:
            A_dict[A[i][j]] += 10**(len(A[i])-j-1)
        else:
            A_dict[A[i][j]] = 10**(len(A[i])-j-1)

for i in A_dict.values():
    numList.append(i)

numList.sort(reverse=True)

total = 0
p = 9
for i in numList:
    total += p * i
    p -= 1
print(total)