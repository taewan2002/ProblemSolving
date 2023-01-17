import sys
from collections import deque
import heapq
import itertools
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def star(n):
    if n == 3:
        return ["***", "* *", "***"]

    arr = star(n//3) # 9
    stars = []
    for i in arr:
        stars.append(i*3)
    for i in arr:
        stars.append(i+" "*(n//3)+i)
    for i in arr:
        stars.append(i*3)
    return stars  

n = int(input())
print('\n'.join(star(n)))