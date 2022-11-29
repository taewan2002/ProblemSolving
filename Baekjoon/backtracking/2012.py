n = int(input())
expected = []
for _ in range(n):
    expected.append(int(input()))

# 정렬
expected.sort()

# 불만족도 합
result = 0
for i in range(1, n+1):
    result += abs(i-expected[i-1])

print(result)