import sys
input = sys.stdin.readline

Alist = list(map(int, input().split()))
Blist = list(map(int, input().split()))
Alist.sort(reverse=True)
Blist.sort(reverse=True)
total = 0
for i in range(len(Alist)):
    total += Alist[i] * Blist[i]
print(total)