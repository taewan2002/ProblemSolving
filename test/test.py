import sys
from collections import deque
import heapq
import itertools
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


arr = []
for _ in range(5):
    arr.append(list(input()[:-1]))

for i in range(15):
    for j in range(5):
        if i < len(arr[j]):
            print(arr[j][i], end="")
print()