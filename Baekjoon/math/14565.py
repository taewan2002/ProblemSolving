# egcd = extended gcd
# d = gcd(a, b)
# ax + by = d
# 적당한 x, y를 찾아서 리턴
# 최소공배수 = a * b / gcd(a, b)에서 반복됨

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = egcd(b, a % b)
        return d, y, x - (a // b) * y

a, b = map(int, input().split())
d, x, y = egcd(a, b)

print(f"d = {d}, x = {x}, y = {y}")
