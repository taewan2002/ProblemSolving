import sys
input = sys.stdin.readline

n = int(input())
total = {}
for _ in range(n):
    tmp = int(input())
    if tmp in total:
        total[tmp] += 1
    else:
        total[tmp] = 1

# value는 높은 순서대로, key는 낮은 순서대로
print(sorted(total.items(), key = lambda x : (-x[1],x[0]))[0][0])