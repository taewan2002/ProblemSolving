import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
g = [[]for _ in range(N+1)] # row는 부모노드, col은 부모노드가 가지는 자식들
for _ in range(N-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

q = deque()
q.append(1) # 1부터 탐색

print(g)

v = [0 for _ in range(N+1)]
while q:
    tmp = q.popleft()
    for nx in g[tmp]:
        if v[nx] == 0: # 방문여부 확인
            v[nx] = tmp # 부모노드 위치 저장
            q.append(nx)

for i in v[2:]: #2번 노트부터 출력
    print(i)