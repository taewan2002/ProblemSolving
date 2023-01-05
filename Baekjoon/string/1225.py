import sys
input = sys.stdin.readline
max = 0

n1, n2 = input().split()
n1 = list(map(int, n1))
n2 = list(map(int, n2))
print(sum(n1) * sum(n2))