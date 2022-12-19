import sys
from collections import deque

t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip() # R, D
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",") # 괄호제거, 콤마제거
    queue = deque(arr)

    rev, front, back = 0, 0, len(queue)-1
    flag = 0
    if n == 0:
        queue = []
        front = 0
        back = 0

    for j in p:
        if j == 'R':
            rev += 1 # 뒤집기 횟수
        elif j == 'D': # 삭제
            if len(queue) < 1: # 빈 배열
                flag = 1
                print("error") # error 출력
                break
            else:
                if rev % 2 == 0:
                    queue.popleft() # 뒤집기 횟수가 짝수면 앞에서부터 삭제
                else:
                    queue.pop() # 뒤집기 횟수가 홀수면 뒤에서부터 삭제
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(queue) + "]") # 뒤집기 횟수가 짝수면 그대로 출력
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]") # 뒤집기 횟수가 홀수면 뒤집어서 출력