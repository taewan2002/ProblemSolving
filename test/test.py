import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
maxValue = int(input())
arr.sort()
start, end = 0, arr[-1]
mid = 0
while start<=end:
    mid = (start+end)//2
    total = []
    for i in arr:
        total.append(min(i, mid))
    if sum(total) <= maxValue:
        start = mid + 1
    else:
        end = mid - 1
print(end)