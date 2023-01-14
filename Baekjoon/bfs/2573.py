import sys
from collections import deque
import pprint
input = sys.stdin.readline

N, M  = map(int, input().split())
G = []
for _ in range(N):
    G.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(i, j):
    q = deque()
    q.append([i,j])

    while q:
        x, y = q.popleft()
        v[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if G[nx][ny] != 0 and not v[nx][ny]:
                    q.append([nx, ny])
                    v[nx][ny] = True
                elif G[nx][ny] == 0:
                    count[x][y] += 1

year = 0
while True:
    iceberg = 0 # 빙산의 수
    v = [[False for _ in range(M)]for _ in range(N)]
    count = [[0 for _ in range(M)]for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if G[i][j] != 0 and not v[i][j]:
                bfs(i, j)
                iceberg += 1
    for i in range(N):
        for j in range(M):
            G[i][j] -= count[i][j]
            if G[i][j] < 0:
                G[i][j] = 0
    if iceberg >= 2:
        print(year)
        break
    elif iceberg == 0: # 빙산이 다 녹았을 때
        print(0)
        break
    year += 1