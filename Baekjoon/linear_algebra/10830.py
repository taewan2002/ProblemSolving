import sys
from collections import deque
import heapq
import itertools
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def mul(n, matrix1, matrix2):
    t = [[0 for _ in range(N)]for _ in range(N)]

    for n in range(N):
        for k in range(N):
            for m in range(N):
                t[n][k] += matrix1[n][m]*matrix2[m][k]
            t[n][k] %= 1000
    return t

def devide(n, b, matrix):
    if b == 1:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] %= 1000
        return matrix
    else:
        tmp = devide(n, b//2, matrix) # 제곱수를 반 나눈 걸로 다시 실행
        # 10 -> 5 -> 2, 2의 배수로 제곱 리턴하고(n^2) -> n^5 -> n^10 완성
        if b%2 == 0: # 2의 배수면
            return mul(n, tmp, tmp) # 제곱을 리턴함
        else:
            return mul(n, mul(n, tmp, tmp), matrix) # 제곱한거에 제곱을 리턴함


N, B = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

total = devide(N, B, A)
for i in total:
    print(*i)