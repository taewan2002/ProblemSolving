import sys
input = sys.stdin.readline

n = 1
while True:
    L, P, V = map(int, input().split())
    if L==0:
        break
    total = 0
    total += V // P * L
    total += min(L, V % P)
    print(f"Case {n}: {total}")
    n+=1