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
            # 오른쪽 문자만 제거하고 회문이 되는지 확인
            if start < end - 1:
                tmp = s[:end] + s[end+1:]
                if tmp[:] == tmp[::-1]:
                    print(1)
                    break
            # 왼쪽 문자만 제거하고 회문이 되는지 확인
            if start + 1 < end:
                tmp = s[:start] + s[start+1:]
                if tmp[:] == tmp[::-1]:
                    print(1)
                    break
            # 회문이 아니면 2
            print(2)
            break
    if start >= end: # 회문이면 0
        print(0)
