import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
parr = [0 for _ in range(N)]
sarr = sorted(arr)
for i in range(len(sarr)):
    parr[arr.index(sarr[i])] = i
    arr[arr.index(sarr[i])] = -1
print(*parr)