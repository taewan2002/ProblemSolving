import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())
G = []
for _ in range(N):
    G.append(list(input().rstrip()))

def bfs(G, i, j):
    V[i][j] = True
    q = deque()
    q.append([i, j]) # 시작 좌표
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if G[x][y] == G[nx][ny] and not V[nx][ny]:
                    V[nx][ny] = True
                    q.append([nx, ny])

total = 0
V = [[False for _ in range(N+1)]for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        if not V[i][j]: # 방문하지 않은 좌표면
            bfs(G, i, j)
            total += 1
print(total)

for i in range(N):
    for j in range(N):
        if G[i][j]=='R': # R의 값을 다 G로 바꿔준다.
            G[i][j]='G'

total = 0
V = [[False for _ in range(N+1)]for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        if not V[i][j]: # 방문하지 않은 좌표면
            bfs(G, i, j)
            total += 1
print(total)