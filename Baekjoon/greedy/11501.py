import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    total = 0
    max_day = arr[-1]
    for i in range(N-2, -1, -1):
        if arr[i] > max_day:
            # 최고점값 갱신
            max_day = arr[i]
        else:
            # 최고점 - 현재 가격 = 실현손익
            total += max_day-arr[i]
    print(total)