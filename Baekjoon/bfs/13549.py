import sys
from collections import deque
input = sys.stdin.readline

MAX = 100001
table = [-1 for _ in range(MAX)]
N, K = map(int, input().split())

cnt = 0
q = deque()
q.append(N)
table[N] = 0

while q:
    x = q.popleft()
    if x == K:
        print(table[K])
        break
    for nx in [x-1, x+1, x*2]:
        if 0 <= nx < MAX:
            if table[nx] == -1 or table[nx] >= table[x]+1:
                if nx == x*2:
                    table[nx] = table[x]
                else:
                    table[nx] = table[x] + 1 # 깊이 기록
                q.append(nx)