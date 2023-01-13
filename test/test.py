import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

# a + b > c
cnt = 0
for a in range(1, N):
    for b in range(a, N):
        c = N - a - b
        if b > c: break # b가 가장 긴변일 때 만 확인함
        if a + b > c: 
            cnt += 1
print(cnt)