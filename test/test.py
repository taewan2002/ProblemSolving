import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
lis = []

for i in arr:
    idx = bisect_left(lis, i)
    if len(lis) <= idx:
        lis.append(i)
    else:
        lis[idx] = i
print(len(lis))