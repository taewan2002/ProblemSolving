import sys
input = sys.stdin.readline

N = int(input())
p = list(map(int, input().split()))
check = []

p.sort()
minValue = int(10e9)
for i in range(N-2):
    fix = p[i]
    start = i+1
    end = N-1
    while start<end:
        tmp = fix + p[start] + p[end]
        if minValue > abs(tmp):
            minValue = abs(tmp)
            check.append([fix, p[start], p[end]])
        if tmp < 0:
            start += 1
        elif tmp > 0:
            end -= 1
print(*check[-1])

# -97 -6 -2 6 98