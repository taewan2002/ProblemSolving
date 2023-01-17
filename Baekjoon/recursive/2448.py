import sys
from collections import deque
import heapq
import itertools
import math
# https://ku-hug.tistory.com/149
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
star = [[' ' for _ in range(N*2)] for _ in range(N)]

def go(x, y, n):
    if n <= 3:
        for i in range(3):
            for j in range(i+1):
                star[x+i][y+j] = star[x+i][y-j] = '*'
        star[x+1][y] = ' '
        return
    m = n // 2
    go(x, y, m) # 0 5 6
    go(x+m, y-m, m) # 6 -1 6 
    go(x+m, y+m, m) # 6 11 6

go(0, N-1, N)

for i in range(N):
    print("".join(star[i]))