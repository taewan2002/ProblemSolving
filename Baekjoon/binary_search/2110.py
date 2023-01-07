import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()
start, end = 1, house[-1] - house[0] # 최소거리, 최대거리
total = 0
# [1, 2, 4, 8, 9]

if C == 2:
    print(end)
else:
    while start < end:
        mid = (start + end)//2 # 간격 설정(?)
        cnt=1
        ts = house[0] # 마지막으로 설치된 공유기 위치
        for i in range(N):
            if house[i] - ts >= mid:
                cnt+=1
                ts = house[i]
        if cnt >= C:
            total = mid
            start = mid + 1 # 공유기 갯수가 넘으면 간격을 넓힌다
        else:
            end = mid # 공유기 갯수가 모자라면 간격을 좁힌다
    print(total)