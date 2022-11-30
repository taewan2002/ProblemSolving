n = int(input())

for i in range(n):
    total = 0
    n, m = map(int, input().split())
    for j in range(n,m+1):
        w = str(j)
        total += w.count('0')
    print(total)