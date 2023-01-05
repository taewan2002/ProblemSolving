import sys
input = sys.stdin.readline

N = int(input())
mlist = []
for i in range(N):
    tmp = list(map(int, input().split()))
    max = 0
    for k in range(3):
        for j in range(k+1, 4):
            for p in range(j+1, 5):
                tmax = tmp[k]+tmp[j]+tmp[p]
                if str(max)[-1] < str(tmax)[-1]:
                    max = tmax
    mlist.append(int(str(max)[-1]))

max = 0
save = 0
for i in range(len(mlist)):
    if mlist[i] >= max:
        max = mlist[i]
        save = i
print(save+1)