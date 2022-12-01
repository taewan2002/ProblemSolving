n = int(input())
num = list(map(int, input().split()))

total_list = []

def dfs(idx, sum):
    global total_list
    if idx == n:
        return 
    
    sum += num[idx]
    total_list.append(sum)
    
    dfs(idx + 1, sum)
    dfs(idx + 1, sum - num[idx])

dfs(0, 0)

def check(total_list):
    for i in range(1, max(total_list)+1):
        if i not in total_list:
            print(i)
            return
    return print(i+1)

check(total_list)


# n = int(input())
# array = list(map(int, input().split()))
# array.sort()

# num = 1

# for i in array:
#     if num < i:
#         break
#     num += i

# print(num)

# Compare this snippet from Baekjoon/sorting/23900.py: