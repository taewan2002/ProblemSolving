import sys
# from collections import deque
import heapq
# import itertools
# import math
# import bisect
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = sys.maxsize

def postfix(post):
    stack = list()

    for i in range(len(post) - 1):
        if (post[i] == "("):
            stack.append(post[i])
        elif (post[i] == "+" or post[i] == "-"):
            while(stack and stack[-1]!='('):
                print(stack.pop(), end="")
            stack.append(post[i])
        elif (post[i] == "*" or post[i] == "/"):
            while (stack and stack[-1] != '(' and (stack[-1] == "*" or stack[-1] =='/')):
                print(stack.pop(), end="")
            stack.append(post[i])
        elif (post[i] == ")"):
            while (stack and stack[-1] != '('):
                print(stack.pop(), end="")
            stack.pop()
        elif (post[i] >= 'A' and post[i] <= 'Z'):
            print(post[i], end="")

    if (len(stack) >0):
        for i in range(len(stack)):
            print(stack.pop(), end="")

postfix(input())