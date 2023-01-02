import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A, B = input().split()
    list = []
    for i in range(len(A)):
        if ord(A[i]) > ord(B[i]):
            list.append(26-(ord(A[i]) - ord(B[i])))
        else:
            list.append((ord(B[i]) - ord(A[i])))
    print("Distances:",*list)