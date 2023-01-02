import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
cnt = 0
high = 0
total = 0
for i in arr:
    if i > high:
        high = i
        cnt = 0
    else:
        cnt += 1
    total = max(total, cnt)

print(total)