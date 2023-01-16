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

N = int(input())
star = []
for i in range(N):
    a, b, c = map(int ,input().split())
    star.append([a, b, c, i]) # i 번째 행성

node = [] # 각 좌표별로 연결 했기 때문에, N-1 * 3 개의 연결 발생
for i in range(3):
    star.sort(key=lambda x: x[i]) # 각 좌표별 정렬
    b = star[0][3] # 이전 행성 번호
    for j in range(1, N):
        c = star[j][3] # 현재 행성 번호
        node.append([b, c, abs(star[j][i]-star[j-1][i])])
        b = c
node.sort(key=lambda x: x[2]) # 코스트가 낮은 순으로 정렬

parent = [i for i in range(N)]

total = 0
for a, b, cost in node:
    if not same_parent(a, b): # 연결돼 있지 않으면 연결 시켜주고
        union_parant(a, b)
        total += cost # 코스트를 더한다
print(total)