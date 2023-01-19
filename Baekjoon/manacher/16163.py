import sys
from collections import deque
import heapq
import itertools
import math
import bisect
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# https://www.crocus.co.kr/1075

def manacher(s):
    N = len(s)
    pal = [0 for _ in range(N)]
    center = 0 # 중심점
    long = 0 # 펠린드롬 값
    total = 0 # 총 펠린드롬 갯수

    for cur in range(N): # cur을 중심으로 펠린드롬 만들기
        if s[cur] != "#": # "#" 이 아니면 스스로도 펠린드롬이다.
            total += 1
        if long < cur: 
            pal[cur] = 0
        else:
            pal[cur] = min(pal[2*center - cur], long - cur)
            total += pal[cur] // 2 # aabcc -> aabcc, abc 펠린드롬이다.

        while cur - pal[cur] - 1 >= 0 and cur + pal[cur] + 1 < N and \
            s[cur-pal[cur]-1] == s[cur+pal[cur]+1]: # 앞 뒤 문자가 같으면
            pal[cur] += 1 # pal값 + 1
            if s[cur + pal[cur]] != "#":
                total += 1

        if long < cur + pal[cur]:
            long = cur + pal[cur]
            center = cur
    return total

print(manacher('#' + '#'.join(input()[:-1]) +'#')) # abc -> #a#b#c#