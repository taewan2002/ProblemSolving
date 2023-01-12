import sys
input = sys.stdin.readline

tmp = 1
total = 0
stack = []

S = input().strip()
for i in range(len(S)):
    if S[i] == "(":
        tmp *= 2
        stack.append(S[i])
    elif S[i] == "[":
        tmp *= 3
        stack.append(S[i])
    elif S[i] == ")":
        if not stack or stack[-1] == "[":
            total = 0
            break
        if S[i-1] == "(":
            total += tmp
        tmp //= 2
        stack.pop()
    else:
        if not stack or stack[-1] == "(":
            total = 0
            break
        if S[i-1] == "[":
            total += tmp
        tmp //= 3
        stack.pop()

if stack:
    total = 0
print(total)