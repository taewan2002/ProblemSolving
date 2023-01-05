import sys
input = sys.stdin.readline

N, M = map(int, input().split())
for _ in range(N):
    tmp = list(input()[:-1])
    for i in range(M):
        if tmp[i] != ".":
            tmp[-(i+1)] = tmp[i]
    for i in tmp:
        print(i, end="")
    print()