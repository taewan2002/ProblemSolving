import math
import sys
input = sys.stdin.readline

A, B = map(int, input().split())
print("1" * math.gcd(A, B))