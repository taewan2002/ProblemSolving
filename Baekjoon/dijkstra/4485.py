import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 

def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0)) # cost, x, y
    distance[0][0] = 0 # 시작점

    while q: # q가 비어있지 않다면
        cost, x, y = heapq.heappop(q) # cost, x, y
        if x == n - 1 and y == n - 1: # 도착점
            print(f'Problem {count}: {distance[x][y]}')
            break
        for i in range(4):
            new_x = x + dx[i] # 다음 x좌표
            new_y = y + dy[i] # 다음 y좌표
            if 0 <= new_x < n and 0 <= new_y < n: # 범위 안에 있다면
                new_cost = cost + graph[new_x][new_y] # 새로운 cost
                if new_cost < distance[new_x][new_y]: # 새로운 cost가 기존 cost보다 작다면
                    distance[new_x][new_y] = new_cost # 기존 cost를 새로운 cost로 갱신
                    heapq.heappush(q, (new_cost, new_x, new_y)) # q에 새로운 cost, x, y를 넣음

count = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]
    dijkstra()
    count += 1