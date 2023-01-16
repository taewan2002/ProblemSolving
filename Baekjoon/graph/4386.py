import sys
from collections import deque
import heapq
import pprint
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

def distance(a, b):
    return math.sqrt((star[a][0] - star[b][0])**2 + (star[a][1] - star[b][1])**2)

N = int(input())
star = []
for _ in range(N):
    a, b = map(float ,input().split())
    star.append([a, b])

node = []
for i in range(N-1):
    for j in range(i+1, N):
        node.append([i, j, distance(i, j)])
node.sort(key=lambda x: x[2]) # 코스트가 낮은 순으로 정렬

parent = [i for i in range(N+1)]

total = 0
for a, b, cost in node:
    if not same_parent(a, b): # 연결돼 있지 않으면 연결 시켜주고
        union_parant(a, b)
        total += cost # 코스트를 더한다
print(round(total,2))