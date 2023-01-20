import sys
# from collections import deque
# import heapq
# import itertools
# import math
# import bisect
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
cycle = (N-1)*2 + (M-1) *2 # 둘레 만큼 회전하면 제자리

for i in range(min(N,M)//2):
    for _ in range(R%(cycle-8*i)): # 한칸 안으로 들어갈 때 마다 cycle이 8씩 감소함
        xshift, yshift = i, i
        shiftValue = table[xshift][yshift]

        for j in range(i+1, N-i): # 좌
            xshift = j
            pValue = table[xshift][yshift] # 이전데이터
            table[xshift][yshift] = shiftValue
            shiftValue = pValue
        
        for j in range(i+1, M-i): # 하
            yshift = j
            pValue = table[xshift][yshift] # 이전데이터
            table[xshift][yshift] = shiftValue
            shiftValue = pValue
        
        for j in range(i+1, N-i): # 우
            xshift = N - j - 1
            pValue = table[xshift][yshift] # 이전데이터
            table[xshift][yshift] = shiftValue
            shiftValue = pValue
        
        for j in range(i+1, M-i): # 상
            yshift = M - j - 1
            pValue = table[xshift][yshift] # 이전데이터
            table[xshift][yshift] = shiftValue
            shiftValue = pValue

for i in table:
    print(*i)