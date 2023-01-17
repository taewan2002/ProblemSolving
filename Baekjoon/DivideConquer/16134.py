import sys
from collections import deque
import heapq
import itertools
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
p = 1000000007

def factorial(N):
    n=1
    for i in range(2, N+1):
        n = (n*i) % p # 1 2 6 24 ...
    return n

def devide(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    else:
        tmp = devide(n, k//2) # 제곱수를 반 나눈 걸로 다시 실행
        # 10 -> 5 -> 2, 2의 배수로 제곱 리턴하고(n^2) -> n^5 -> n^10 완성
        if k%2: # 2의 배수가 아니면
            return tmp * tmp * n % p
        else:
            return tmp * tmp % p


N, K = map(int, input().split())
# nCr = N! / (N-K)! * K!

# 페르마의 소정리
# p가 소수, a가 정수일 때
# a^p = a(mod p)
# a^(p-2) = 1/a(mod p)
# a^-1은 a^(p-2)와 합동

top = factorial(N)
bot = factorial(N-K) * factorial(K) % p

print(top * devide(bot, p-2) % p)