import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int, input().split())

q = deque()
q.append([A,1])
while q:
    a, v = q.popleft()
    if a > B:
        continue
    if a == B:
        print(v)
        break
    q.append([a*2, v+1])
    q.append([int(str(a)+"1"), v+1])
else:
    print(-1)

# import sys
# from collections import deque
# input = sys.stdin.readline

# A, B = map(int, input().split())

# g = [-1 for _ in range(B+1)]

# q = deque()
# q.append(A)
# g[A] = 1

# while q:
#     tmp = q.popleft()
#     for i in range(2):
#         if i == 0:
#             if tmp*2 <= B:
#                 q.append(tmp*2)
#                 g[tmp*2] = g[tmp]+1
#         else:
#             newtmp = int(str(tmp)+"1")
#             if newtmp <= B:
#                 q.append(newtmp)
#                 g[newtmp] = g[tmp]+1

# print(g[B])