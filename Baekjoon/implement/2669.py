import sys
input = sys.stdin.readline

table = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            table[i][j] = 1
total = 0
for row in table:
    total += sum(row)
print(total)