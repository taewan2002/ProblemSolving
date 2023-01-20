import sys
# from collections import deque
# import heapq
# import itertools
# import math
# import bisect
# sys.setrecursionlimit(10**6)
# https://www.acmicpc.net/problem/16935
input = sys.stdin.readline

def f1():
    newTable = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        newTable[i] = arr[n-i-1]
    return newTable

def f2():
    newTable = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            newTable[i][j] = arr[i][m-j-1]
    return newTable

def f3():
    newTable = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            newTable[i][j] = arr[n-j-1][i]
    return newTable

def f4():
    newTable = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            newTable[i][j] = arr[j][m-i-1]
    return newTable

def f5():
    newTable = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n//2): # 1 -> 2
        for j in range(m//2):
            newTable[i][j+m//2] = arr[i][j]
    for i in range(n//2): # 2 -> 3
        for j in range(m//2,m):
            newTable[i+n//2][j] = arr[i][j]
    for i in range(n//2,n): # 3 -> 4
        for j in range(m//2,m):
            newTable[i][j-m//2] = arr[i][j]
    for i in range(n//2,n): # 4 -> 1
        for j in range(m//2):
            newTable[i-n//2][j] = arr[i][j]
    return newTable

def f6():
    newTable = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n//2): # 1 -> 4
        for j in range(m//2):
            newTable[i+n//2][j] = arr[i][j]
    for i in range(n//2,n): # 4 -> 3
        for j in range(m//2):
            newTable[i][j+m//2] = arr[i][j]
    for i in range(n//2,n): # 3 -> 2
        for j in range(m//2,m):
            newTable[i-n//2][j] = arr[i][j]
    for i in range(n//2): # 2 -> 1
        for j in range(m//2,m):
            newTable[i][j-m//2] = arr[i][j]
    return newTable

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
operation = list(map(int, input().split()))

for oper in operation:
    if oper == 1:
        arr = f1()
    elif oper == 2:
        arr = f2()
    elif oper == 3:
        arr = f3()
        n, m = m, n
    elif oper == 4:
        arr = f4()
        n, m = m, n
    elif oper == 5:
        arr = f5()
    else:
        arr = f6()
 
for i in arr:
    print(*i)