import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
stack = []
st = [0 for _ in range(N)]

for i in range(N):
    t = arr[i]
    while stack and arr[stack[-1]] < t:
        stack.pop()
    if stack:
        st[i] = stack[-1] + 1
    stack.append(i)

print(*st)