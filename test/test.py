import sys
from collections import deque
import heapq
import itertools
import math
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
table = [list(input())for _ in range(N)]
maxCnt = 0

def check():
    global maxCnt
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if table[i][j] == table[i][j-1]:
                cnt += 1
                maxCnt = max(cnt, maxCnt)
            else:
                cnt = 1
        cnt = 1
        for j in range(1, N):
            if table[j][i] == table[j-1][i]:
                cnt += 1
                maxCnt = max(cnt, maxCnt)
            else:
                cnt = 1
                
for i in range(N):
    for j in range(N):
        if j + 1 < N:
            table[i][j], table[i][j+1] = table[i][j+1], table[i][j]
            check()
            table[i][j], table[i][j+1] = table[i][j+1], table[i][j]
        if i + 1 < N:
            table[i][j], table[i+1][j] = table[i+1][j], table[i][j]
            check()
            table[i][j], table[i+1][j] = table[i+1][j], table[i][j]

print(maxCnt)