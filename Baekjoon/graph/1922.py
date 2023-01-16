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

V = int(input())
E = int(input())
edges = []
for _ in range(E):
    a, b, c = map(int ,input().split())
    edges.append([a, b, c])
edges.sort(key=lambda x: x[2]) # 가중치가 낮은것부터 정렬
# 가중치가 낮은 순서부터 연결하기 때문에 최소 스패닝 트리가 만들어 진다.

parent = [i for i in range(V+1)]

total = 0
for a, b, cost in edges:
    if not same_parent(a, b): # 연결돼 있지 않으면 연결 시켜주고
        union_parant(a, b)
        total += cost # 코스트를 더한다
print(total)