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

def getDist(p1,p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

N, L = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(N)]
c = convex_hull(points) # 볼록껍질을 이루는 점들
total = 0
for i in range(len(c)):
    total += getDist(c[i-1], c[i]) # 볼록 껍질을 이루는 점들의 길이를 다 더함
total += math.pi*L*2 # 만약 N이 4면, 4면을 더하고 1/4씩 각 모퉁이를 더하는거랑 같음
print(f"{total:.12f}")