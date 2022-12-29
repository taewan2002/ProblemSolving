import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 후위 순회, postorder
# 왼쪽 서브트리 -> 오른쪽 서브트리 -> 루트 노드
# 왼쪽 서브트리의 루트 노드 < 루트 노드 < 오른쪽 서브트리의 루트 노드

def postorder(start, end):
    # end = 마지막 인덱스
    if start > end:
        return
    root = num_list[start] # 현재 노드
    for i in range(start + 1, end + 1): 
        if root < num_list[i]: # 오른쪽 서브트리
            postorder(start + 1, i - 1) # 왼쪽 서브트리
            postorder(i, end) # 오른쪽 서브트리
            print(root)
            return
    # 오른쪽 서브트리가 없는 경우
    postorder(start + 1, end) # 왼쪽 서브트리
    print(root) # 루트 노드 출력

num_list = []
while True:
    # 입력이 주어지지 않으면 postorder 함수를 호출한다.
    try:
        num = int(input())
        num_list.append(num)
    except:
        postorder(0, len(num_list) - 1)
        break


