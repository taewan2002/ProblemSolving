import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

total = [0 for _ in range(101)]
S = {} # 사다리
D = {} # 뱀
V = [False for _ in range(101)]
for _ in range(N):
    a, b = map(int, input().split())
    S[a] = b
for _ in range(M):
    a, b = map(int, input().split())
    S[a] = b

q = deque()
q.append(1)
while q:
    tmp = q.popleft()
    for i in range(1, 7): # 주사위
            check = tmp + i
            if 0 < check <= 100 and not V[check]:
                if check in S.keys():
                    check = S[check] # 사다리 타기
                if check in D.keys():
                    check = D[check] # 되돌아가기
                if not V[check]:
                    q.append(check)
                    V[check] = True # 방문 처리
                    total[check] = total[tmp] + 1
print(total[100])