import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    stack = list(input().split())
    stack.reverse()
    print(f"Case #{i+1}:", *stack)