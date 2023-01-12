import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    s = input().strip()
    start = 0
    end = len(s)-1
    while start<end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            if start < end - 1:
                tmp = s[:end] + s[end+1:]
                if tmp[:] == tmp[::-1]:
                    print(1)
                    break
            if start + 1 < end:
                tmp = s[:start] + s[start+1:]
                if tmp[:] == tmp[::-1]:
                    print(1)
                    break
            print(2)
            break
    if start >= end:
        print(0)