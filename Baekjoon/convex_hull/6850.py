import sys
from collections import deque
import heapq
import itertools
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def convex_hull(points):
    points = sorted(points)
    lower = [] # 왼쪽에서 오른쪽으로
    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0: # <= 0 이면 같은 직선에 있는 점도 포함
            lower.pop()
        lower.append(p)
    upper = [] # 오른쪽에서 왼쪽으로
    for p in reversed(points):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1] # 시작점과 끝점이 중복되므로 제거

# N = int(input())
# for _ in range(N):
k = int(input())
points = [list(map(int, input().split())) for _ in range(k)]
c = convex_hull(points) # 볼록껍질을 이루는 점들
total = 0
for i in range(len(c)):
    total += (c[i-1][0]*c[i][1]) - (c[i][0]*c[i-1][1]) # 다각형의 넓이 구하기
total = abs(total)//100 # 2로 나누고 50으로 나눠야 하기에 100으로 나눔
print(total)