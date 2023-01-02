import sys
input = sys.stdin.readline

s = list(input())[:-1]

for i in s:
    cnt = 0
    for k in str(ord(i)):
        cnt += int(k)
    print(i * cnt)