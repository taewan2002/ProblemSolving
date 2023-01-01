import sys
input = sys.stdin.readline

n = int(input())
total = []
for _ in range(n):
    a, b = input().split()
    total.append([a, int(b)])

# value는 높은 순서대로, key는 낮은 순서대로
print(sorted(total, key = lambda x : (-x[1],x[0]))[0][0])