import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
if M:
    broken = list(map(int, input().split()))
else:
    broken = []

target = abs(100 - N)
for i in range(1000001):
    num = str(i)
    for k in range(len(num)):
        if int(num[k]) in broken:
            break
        elif k == len(num)-1:
            target = min(target, abs(i - N) + len(num))

print(target)