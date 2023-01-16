import sys
from collections import deque
import heapq
import itertools
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
dice = list(map(int, input().split()))

if N == 1:
    print(sum(dice)-max(dice))
else:
    sumList = [min(dice[0], dice[5]),
               min(dice[1], dice[4]),
               min(dice[2], dice[3])]
    sumList.sort()

    n1 = (N-1)*(N-2)*4 + (N-2)**2 # 바닥에 붙어있는 4면 + 윗면
    n2 = (N-2)*4 + (N-1)*4 # 바닥에 붙어있는 4면 + 위에 4면
    n3 = 4 # 윗쪽 모퉁이 4개 
    
    print(n1 * sumList[0] + n2 * sum(sumList[:2]) + n3 * sum(sumList))