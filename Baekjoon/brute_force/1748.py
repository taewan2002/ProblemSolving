import sys
from collections import deque
import heapq
import itertools
import math
import bisect
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

total = 0
for i in range(len(str(N))-1):
    total += 9 * int((math.pow(10, i))) * (i+1)
total += (N-int(math.pow(10, len(str(N))-1)) + 1) * len(str(N))
print(total)