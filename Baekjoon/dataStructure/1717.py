import sys
from collections import deque
import heapq
import pprint
import itertools
import math
input = sys.stdin.readline

N, M = map(int, input().split())

node = [i for i in range(N+1)]

def get_parent(x):
    if node[x] == x: # 자기 스스로가 될때 까지 -> 연결의 끝까지 검색
        return x
    node[x] = get_parent(node[x]) # 재귀로 연결된 끝까지 감
    return node[x]

def union_parant(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b: # 작은 수를 부모로
        node[b] = a
    else:
        node[a] = b

for _ in range(M):
    c, a, b = map(int, input().split())
    if c == 0:
        union_parant(a, b)
    else:
        print("YES" if get_parent(a)==get_parent(b) else "NO")