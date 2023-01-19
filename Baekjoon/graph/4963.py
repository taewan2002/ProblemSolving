import sys
from collections import deque
import heapq
import itertools
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# https://www.acmicpc.net/problem/4963

dx = [1, 1, -1, -1, 1, -1, 0, 0] # 대각선도 접근 가능하게 함
dy = [0, 1, 0, 1, -1, -1, 1, -1]

def dfs(x, y):
  field[x][y] = 0
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
      dfs(nx, ny)

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  field = []
  count = 0
  for _ in range(h):
    field.append(list(map(int, input().split())))
  for i in range(h):
    for j in range(w):
      if field[i][j] == 1: # 섬이라면
        dfs(i, j) # dfs탐색 시작
        count += 1 # 갯수 추가
  
  print(count)