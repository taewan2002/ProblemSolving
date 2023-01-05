import sys
input = sys.stdin.readline

for _ in range(int(input())):
    tmp = input()[:-1]
    for i in range(len(tmp)):
        if i == 0:
            print(tmp[i].upper(), end="")
        else:
            print(tmp[i], end="")
    print()