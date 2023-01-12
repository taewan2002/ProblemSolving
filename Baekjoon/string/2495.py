import sys
input = sys.stdin.readline

for _ in range(3):
    tmpMax = 0
    check = [0 for _ in range(10)]
    s = input().strip()
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            check[int(s[i])] += 1
        else:
            tmpMax = max(tmpMax, max(check)+1)
            check = [0 for _ in range(10)]
    tmpMax = max(tmpMax, max(check)+1)
    print(tmpMax)