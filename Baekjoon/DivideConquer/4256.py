import sys
from collections import deque
import heapq
# import itertools
# import math
# import bisect
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
INF = sys.maxsize

def postorder(root, start, end):
    for i in range(start, end):
        if inorder[i] == preorder[root]:
            postorder(root + 1, start, i) # 왼쪽 서브트리
            postorder(root + i + 1 - start, i + 1, end) # 오른쪽 서브트리
            print(preorder[root], end=" ")
  
for _ in range(int(input())):
    N = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    postorder(0, 0, N)
    print()