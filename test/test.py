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

    if a != b:
        parent[b] = a # 앞이 부모 노드가 됨
        number[a] += number[b] # 연결 노드수 증가

for _ in range(int(input())):
    parent = {}
    number = {}
    for _ in range(int(input())):
        tmp = list(input().split())
        for i in tmp:
            if i not in parent: # 딕셔너리에 추가
                parent[i] = i
                number[i] = 1 # 연결 노드수
        union_parant(tmp[0], tmp[1])
        print(number[get_parent(tmp[0])]) # 부모노드의 연결 수     
        