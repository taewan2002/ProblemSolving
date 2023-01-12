import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우로 탐색하기 위함
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip()))) # 0000 -> [0, 0, 0, 0]


def bfs(graph, a, b): # 넓이 우선 탐색
    q = deque()
    q.append([a, b]) # [a, b] 는 좌표값
    cnt = 1 # 몇개의 1이 이어져 있는지 확인하기 위함

    while q:
        x, y = q.popleft() # q에 들어있는 값
        graph[x][y] = 0 # 방문 처리
        for i in range(4): # 상 하 좌 우로 1이 있는지 확인
            nx = x + dx[i]
            ny = y + dy[i]

            # 새로운 좌표가 범위를 벗어나는 경우 continue
            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue
            
            if graph[nx][ny] == 1: # 아직 방문 안한 1이라면
                graph[nx][ny] = 0 # 방문 처리
                q.append([nx, ny])
                cnt += 1
    return cnt

total = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1: # 1을 찾으면 그때부터 탐색 시작
            count = bfs(graph, i, j)
            total.append(count)

total.sort()
print(len(total))
for i in total:
    print(i)
