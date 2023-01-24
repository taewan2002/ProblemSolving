import sys
from collections import deque
import heapq
# import itertools
# import math
# import bisect
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
INF = sys.maxsize

def preorder(in_start, in_end, post_start, post_end):
    # 재귀 종료 조건
    if in_start > in_end or post_start > post_end:
        return

    # 후위 순회 결과의 끝이 서브트리의 루트
    parent = postorder[post_end]
    print(parent, end=" ")

    left = position[parent] - in_start
    right = in_end - position[parent]

    preorder(in_start, in_start+left-1, post_start, post_start+left-1) # 왼쪽 서브트리
    preorder(in_end-right+1, in_end, post_end-right, post_end-1) # 오른쪽 서브트리
  
    
N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = [0 for _ in range(N+1)]
# 중위 순회의 값들의 인덱스값을 저장
# 후위 순회는 루트가 마지막에 나온다. 그 위치를 알기 위해 값을 저장한다.
for i in range(N):
    position[inorder[i]] = i

preorder(0, N-1, 0, N-1)