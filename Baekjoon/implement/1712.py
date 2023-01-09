import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
if B >= C:
    print(-1)
else:
    tmp = C-B
    print(A//tmp+1)