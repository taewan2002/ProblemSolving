import sys
input = sys.stdin.readline

N = int(input())
num_list = sorted(list(map(int, input().split())))
min_value = 1e9
for i in range(N):
    if min_value > num_list[i] + num_list[-1-i]:
        min_value = num_list[i] + num_list[-1-i]
print(min_value)