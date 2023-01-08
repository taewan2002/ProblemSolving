import sys
from bisect import bisect_left
# bisect_left(이진 탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다)
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(N)] # 역추적을 위한 dp
lis = []
l = 0
for i in range(N):
    n = arr[i]
    idx = bisect_left(lis, n) # i가 가장 큰 숫자라면
    
    if idx == l: # 가장 큰숫자가 맞으면?
        lis.append(n)
        l += 1
    else:
        lis[idx] = n # 아니면 업데이트
    dp[i] = idx # dp에 저장
print(l) # 길이 출력
toPrint = [] # 역추적
for i in range(N-1, -1, -1):
    if dp[i] == l-1: # dp테이블에서 역추적으로 뽑아옴
        toPrint.append(arr[i])
        l -= 1
print(*reversed(toPrint))