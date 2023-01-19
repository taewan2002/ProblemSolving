import sys
from collections import deque
import heapq
import itertools
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())
name = [0 for _ in range(26)]
for i in range(N):
    name[ord(input()[0])-97] += 1

PREDAJA = False
for i in range(26):
    if name[i] >= 5:
        print(chr(i+97), end="")
        PREDAJA = True
if PREDAJA == False:
    print("PREDAJA")