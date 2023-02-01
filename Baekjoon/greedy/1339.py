import sys
from collections import deque
import heapq
# import itertools
# import math
# import bisect
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
INF = sys.maxsize

def bt(cnt, idx):

    # 암호를 만들었을 때
    if cnt == L:
        # 모음, 자음 체크
        vo, co = 0, 0

        for i in range(L):
            if total[i] in consonant:
                vo += 1
            else:
                co += 1

        if vo >= 1 and co >= 2:
            print("".join(total))
        return
    
    # 반복문을 통해 암호를 만든다
    for i in range(idx, C):
        total.append(W[i])
        bt(cnt+1, i+1)
        total.pop()




L, C = map(int, input().split())
W = sorted(list(input().split()))
# print(W)
consonant = ["a", "e", "i", "o", "u"]
total = []
bt(0,0)