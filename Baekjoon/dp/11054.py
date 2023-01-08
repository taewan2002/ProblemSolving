import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

inc = [1 for _ in range(N)]
dec = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            inc[i] = max(inc[i], inc[j]+1)
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if arr[i] > arr[j]:
            dec[i] = max(dec[i], dec[j]+1)
total = [0 for _ in range(N)]
for i in range(N):
    total[i] = inc[i] + dec[i] - 1

print(max(total))