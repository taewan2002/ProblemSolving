import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
lis = []

# bisect_left(이진 탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다)
for i in arr:
    idx = bisect_left(lis, i)
    if len(lis) <= idx: # i가 가장 큰 숫자라면
        lis.append(i) # 추가
    else:
        lis[idx] = i # 자신보다 큰 수 중 최솟값과 대체
print(len(lis))