n = int(input())

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list1.sort()

total = 0
for i in range(n):
    total += min(list1) * max(list2)
    list1.pop(list1.index(min(list1)))
    list2.pop(list2.index(max(list2)))
    
print(total)

# Compare this snippet from Baekjoon/sorting/23900.py:
