def egcd(a, b):
    if b == 0:
        return  a, 1, 0
    else:
        d, x, y = egcd(b, a % b)
        return d, y, x - (a // b) * y

a, b = map(int, input().split())
d, x, y = egcd(b, a)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

while(x <= 0):
    x += a

if gcd(a, b) != 1:
    print(f"{a-b} -1")
else:
    print(f"{a-b} {x}")
