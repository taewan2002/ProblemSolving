import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    p = []

    K = int(input())
    for _ in range(K):
        p.append(list(map(int, input().split())))
    
    p.sort()
    temp = p[0][1]
    cnt = 1

    for i in range(K):
        # 처음 원소로 이미 정렬을 함
        # = 처음 원소 순위는 밀린다
        # 두번째 원소 순위는 밀리면 안된다
        if temp > p[i][1]:
            cnt +=1
            temp = p[i][1]
    print(cnt)