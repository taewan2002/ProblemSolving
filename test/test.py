import sys
from collections import deque
input = sys.stdin.readline

MAX = 100001
table = [-1 for _ in range(MAX)]
move = [0 for _ in range(MAX)]
N, K = map(int, input().split())

cnt = 0
q = deque()
q.append(N)
table[N] = 0

def path(x): # 부모노드로부터 역추적해서 출력
    arr = []
    tmp = x
    for _ in range(table[x]+1):
        arr.append(tmp)
        tmp = move[tmp]
    arr.reverse()
    print(*arr)


while q:
    x = q.popleft()
    if x == K:
        print(table[K])
        path(x)
        break
    for nx in [x-1, x+1, x*2]:
        if 0 <= nx < MAX:
            if table[nx] == -1 or table[nx] >= table[x]+1:
                table[nx] = table[x] + 1 # 깊이 기록
                q.append(nx)
                move[nx] = x # 부모노드를 기록
