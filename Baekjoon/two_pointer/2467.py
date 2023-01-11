import sys
input = sys.stdin.readline

N = int(input())
p = list(map(int, input().split()))
check = []

start = 0
end = N-1
minValue = abs(p[start] + p[end])
check.append([p[start], p[end]])
while start<end:
    if minValue > abs(p[start] + p[end]):
        minValue = abs(p[start] + p[end])
        check.append([p[start], p[end]])
    if p[start] + p[end] < 0:
        start += 1
    else:
        end -= 1
print(*check[-1])
