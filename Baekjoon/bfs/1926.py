import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
G = []
for _ in range(N):
    G.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(G, i, j):
    q = deque()
    q.append([i, j])
    G[i][j] = 0
    tmp = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if G[nx][ny] == 1:
                    G[nx][ny] = 0
                    q.append([nx, ny])
                    tmp += 1
    return tmp

cnt, total = 0, 0
for i in range(N):
    for j in range(M):
        if G[i][j] == 1:
            total = max(total, bfs(G, i, j))
            cnt += 1
print(cnt)
print(total)