import sys
input = sys.stdin.readline
max = 0

for _ in range(int(input())):
    tmp = input()[:-1]
    if max < tmp.count("while")+tmp.count("for"):
        max = tmp.count("while")+tmp.count("for")
print(max)