import sys
input = sys.stdin.readline

N = int(input())
print(sum(K*(N//K) for K in range(1, N+1)))
# f(1) = 1
# f(2) = 1 + 2
# f(3) = 1 + 3
# f(4) = 1 + 2 + 4
# g(4) = 1*4 + 2*2 + 3 + 4