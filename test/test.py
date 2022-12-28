import sys
input = sys.stdin.readline

def lower_bound(key):
    global total_list
    start = 0
    end = len(total_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if total_list[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return start


def get_max(node):
    global total_list
    global high
    lb = lower_bound(node)
    if lb > 0:
        left = high[total_list[lb - 1]]
    else:
        left = 0
    if lb < len(total_list):
        right = high[total_list[lb]]
    else:
        right = 0
    high[node] = max(left, right) + 1
    total_list.insert(lb, node)

    return high[node]


n = int(input())
total = 0
total_list = []
high = [0] * (n + 1)
for i in range(n):
    total += get_max(int(input()))
print(total)