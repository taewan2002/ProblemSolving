import sys
import math
input = sys.stdin.readline

fnum = [math.factorial(i) for i in range(21)]
# 21! 부터는 범위를 벗어난다.
N = int(input())

if N==0:
    print("NO")
else:
    for i in range(20, -1, -1):
        if N >= fnum[i]:
            N -= fnum[i]
    if N == 0: # N을 fnum원소로 뺏을 때 0이되면 더해서 만들 수 있음
        print("YES")
    else:
        print("NO")