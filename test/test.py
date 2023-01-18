import sys
from collections import deque
import heapq
import itertools
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# https://www.acmicpc.net/problem/20040

n, m = map(int, input().split())
parent = [i for i in range(n)]
endgame = 0

def get_parent(x):
    if parent[x] == x: # 자기 스스로가 될때 까지 -> 연결의 끝까지 검색
        return x
    parent[x] = get_parent(parent[x]) # 재귀로 연결된 끝까지 감
    return parent[x]

def union(x, y, indx):
    global endgame
    x = get_parent(x)
    y = get_parent(y)
    if x != y:
        parent[max(x,y)] = min(x,y)
    elif endgame == 0:
        endgame = indx

for i in range(1, m+1):
    a, b = map(int, input().split())
    union(a, b, i)

print(endgame)