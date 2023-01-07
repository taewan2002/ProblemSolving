import sys
input = sys.stdin.readline
money = [500, 100, 50, 10, 5, 1]

N = 1000 - int(input())
total = 0
for i in money: # 620
    total += N // i
    N %= i
print(total)
