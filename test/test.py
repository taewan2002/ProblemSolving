import sys
from collections import deque
import heapq
import pprint
import itertools
input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))
sumList = sum(numList)
total = 0
for i in numList:
    sumList -= i
    total += i*sumList
    total %= 1000000007
print(total)