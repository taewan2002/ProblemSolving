import sys
from collections import deque
import heapq
import itertools
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
B = []
for _ in range(N):
    A.append(list(map(int, input().split())))
M, K = map(int, input().split())
for _ in range(M):
    B.append(list(map(int, input().split())))

t = [[0 for _ in range(K)]for _ in range(N)]
for n in range(N):
    for k in range(K):
        for m in range(M):
            t[n][k] += A[n][m]*B[m][k]
for i in t:
    print(*i)