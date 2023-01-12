import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우로 탐색하기 위함
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())

graph = []
maxValue = 0
for _ in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for i in tmp:
        maxValue = max(maxValue, i)


def bfs(graph, a, b, safezone, v): # 넓이 우선 탐색
    q = deque()
    q.append([a, b]) # [a, b] 는 좌표값
    v[a][b] = 1
    while q:
        x, y = q.popleft() # q에 들어있는 값
        
        for i in range(4): # 상 하 좌 우로 1이 있는지 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > safezone and v[nx][ny] == 0: # 안전 구역이고 방문하지 않았다면
                    v[nx][ny] = 1 # 방문 처리
                    q.append([nx, ny])

total = 1
for i in range(1, maxValue+1):
    v = [[0 for _ in range(N)] for _ in range(N)] # 방문 확인용
    cnt = 0
    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and v[j][k] == 0: # 방문하지 않았고 안전구역 이라면
                bfs(graph, j, k, i, v)
                cnt += 1
    total = max(total, cnt)
 
print(total)