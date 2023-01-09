import sys
input = sys.stdin.readline

N = int(input())
total = 0
divnum = 10**9+7
for _ in range(N):
    C, X = map(int, input().split())
    if X-1 != 0:
        total += C*X*(2**(X-1)) % divnum
    else:
        total += C*X % divnum
    
print(total%divnum)