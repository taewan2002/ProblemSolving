import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
start = 1 # 이분탐색 시작
end = K # 최대값(원래 N*N인데 더 효율적인 방법)
while start < end:
    mid = (start + end)//2
    
    tmp = 0
    for i in range(1, N+1):
        tmp += min(mid//i, N) # mid이하의 i의 배수 or N
        # 정렬했을 때 자기보다 작은 숫자의 갯수가 K개가 되면 답을 알 수 있다.
    if tmp < K:
        start = mid + 1
    else:
        end = mid
print(start)