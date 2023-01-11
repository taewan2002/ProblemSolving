import sys
input = sys.stdin.readline

N, M = map(int, input().split())
check = [0 for _ in range(N)]
arr = []
while True:
    tmp = list(input().split())
    if tmp[0] == '0':
        break
    k = int(tmp[0])
    if check[k] < M:
        check[k] += 1
        arr.append(tmp)

arr = sorted(arr, key=lambda x: (int(x[0]), len(x[1]), x[1]))
blue = []
white = []

for i in arr:
    if int(i[0])%2==0:
        white.append(i)
    else:
        blue.append(i)

for i in blue:
    print(*i)
for i in white:
    print(*i)