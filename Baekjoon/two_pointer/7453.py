import sys
input = sys.stdin.readline

N = int(input())
tmp, AB, CD = [], [], []
for _ in range(N):
    tmp.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        AB.append(tmp[i][0]+tmp[j][1])
        CD.append(tmp[i][2]+tmp[j][3])

AB.sort()
CD.sort()

start = 0
end = len(AB)-1
total = 0
while start < len(AB) and end >= 0:
    if AB[start] + CD[end] < 0:
        start += 1
    elif AB[start] + CD[end] > 0:
        end -= 1
    else:
        stmp, etmp = start + 1, end - 1
        while stmp < len(AB) and  AB[start] == AB[stmp]:
            stmp += 1
        while etmp >= 0 and CD[end] == CD[etmp]:
            etmp -= 1
        total += (stmp-start) * (end - etmp)
        start = stmp
        end = etmp

print(total)

# import sys
# input = sys.stdin.readline

# N = int(input())
# A, B, C, D = [], [], [], []
# for _ in range(N):
#     a, b, c, d = map(int, input().split())
#     A.append(a)
#     B.append(b)
#     C.append(c)
#     D.append(d)

# ab = {}
# for a in A:
#     for b in B:
#         tmp = a + b
#         if tmp not in ab.keys():
#             ab[tmp] = 1
#         else:
#             ab[tmp] += 1

# total = 0
# for c in C:
#     for d in D:
#         tmp = -1 * (c + d)
#         if tmp in ab.keys():
#             total += ab[tmp]

# print(total)