n = int(input())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    if list1 == list2:
        break
    idx = list1.index(max(list1[:i + 1])) # 최댓값의 인덱스
    if idx != i:
        list1[idx], list1[i] = list1[i], list1[idx]

print(1 if list1 == list2 else 0)