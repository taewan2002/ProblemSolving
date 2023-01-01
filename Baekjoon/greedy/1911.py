import math
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
pool = [list(map(int, input().split())) for _ in range(N)]
pool.sort()

cnt = 0
index = 0
for start, end in pool:
    if start <= index:
        start = index+1

        if end <= start:
            continue
    
    pcnt = math.ceil((end-start)/L)
    cnt += pcnt
    index = max(index, start + pcnt*L-1)

print(cnt)