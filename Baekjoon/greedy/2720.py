import sys
input = sys.stdin.readline

money = [25, 10, 5, 1]
for _ in range(int(input())):
    total = [0 for _ in range(4)]
    
    N = int(input())
    for i in range(4):
        total[i] = N // money[i]
        N %= money[i]
    print(*total)
