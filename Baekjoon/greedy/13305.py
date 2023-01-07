import sys
input = sys.stdin.readline

N = int(input())
node = list(map(int, input().split()))
cost = list(map(int, input().split()))

total = cost[0] * node[0] # 첫 주유
mcost = cost[0] # 싼 주유
for i in range(1, N-1):
    if mcost > cost[i]:
        mcost = cost[i]
    total += mcost * node[i]

print(total)