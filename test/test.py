import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
lis = [0]

# for i in arr:
#     if lis[-1] < i: # 마지막 원소보다 크면 추가
#         lis.append(i)
#     else: # 마지막 원소보다 작으면 업데이트
#         start = 0
#         end = len(lis)
#         while start < end: # 이분탐색
#             mid = (start+end)//2
#             if lis[mid] < i:
#                 start = mid+1
#             else:
#                 end = mid
#         lis[end] = i # 맞는 위치에 추가
# print(len(lis)-1) # lis 자체는 아니지만 길이는 만족

# 모듈 활용
for i in arr:
    if lis[-1] < i:
        lis.append(i)
    else:
        idx = bisect_left(lis, i)
        lis[idx] = i
print(len(lis)-1)

# 모듈 활용이 1032ms, 구현이 4144ms