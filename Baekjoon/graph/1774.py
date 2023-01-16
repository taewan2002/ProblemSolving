import sys
from collections import deque
import heapq
import itertools
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def get_parent(x):
    if parent[x] == x: # 자기 스스로가 될때 까지 -> 연결의 끝까지 검색
        return x
    parent[x] = get_parent(parent[x]) # 재귀로 연결된 끝까지 감
    return parent[x]

def union_parant(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b        


def same_parent(a, b):
    return get_parent(a) == get_parent(b)

def get_cost(x, y):
    return math.sqrt((link[x][0]-link[y][0])**2 +(link[x][1]-link[y][1])**2)

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
link = [[0]]
for _ in range(N):
    x, y = map(int, input().split())
    link.append([x,y]) # 링크 해야될 좌표
for _ in range(M):
    x, y = map(int, input().split())
    if not same_parent(x, y):
        union_parant(x, y) # 미리 연결 시켜놓고 mst 실행

node = []
for i in range(1, N):
    for j in range(i+1, N+1):
        node.append([i, j, get_cost(i, j)])
node.sort(key=lambda x: x[2]) # 코스트가 낮은 순으로 정렬

total = 0
for a, b, cost in node:
    if not same_parent(a, b): # 연결돼 있지 않으면 연결 시켜주고
        union_parant(a, b)
        total += cost # 코스트를 더한다
print(f"{total:.2f}")