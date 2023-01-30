import sys
from collections import deque
import heapq
# import itertools
# import math
# import bisect
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
INF = sys.maxsize

s = input().rstrip()
d = input().rstrip()

stack = []
l = len(d)
for i in range(len(s)):
    stack.append(s[i])
    if "".join(stack[-l:]) == d:
        for _ in range(l):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")