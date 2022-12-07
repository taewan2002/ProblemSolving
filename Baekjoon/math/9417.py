def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


n = int(input())
for i in range(n):
    list_num = list(map(int, input().split()))
    list_num.sort()
    max_num = []
    for j in range(len(list_num)):
        for k in range(len(list_num)):
            if j <= k:
                continue
            else:
                max_num.append(gcd(list_num[j], list_num[k]))
    print(max(max_num))

# Path: Baekjoon/math/14565.py