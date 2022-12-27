# https://www.acmicpc.net/problem/10217
# KCM Travel
# 시간제한 : 2초, 메모리 제한 : 256MB

# 반례
# 입력
# 1
# 6 149 8
# 1 2 60 20
# 2 3 30 70
# 1 3 100 80
# 1 3 20 180
# 3 4 20 100
# 3 5 150 20
# 5 6 50 40
# 4 6 30 50
# 출력
# 240

# 코드
import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost <= m and cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [sys.maxsize] * (n+1)
    for _ in range(k):
        u, v, c, d = map(int, input().split())
        graph[u].append((v, c, d))
    dijkstra(1)
    if distance[n] == sys.maxsize:
        print('Poor KCM')
    else:
        print(distance[n])

