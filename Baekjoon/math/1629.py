def power(a, b, c):
    if b == 1: # b의 값이 1이면 a % c를 return한다.
        return a % c
    else:
        temp = power(a, b // 2, c) # a^(b // 2)를 미리 구한다.
        if b % 2 == 0:
            return temp * temp % c # b가 짝수인 경우
        else:
            return temp * temp * a % c # b가 홀수인 경우


a, b, c = map(int, input().split())
print(power(a, b, c))

# 분할정복을 이용한 거듭제곱
# 1. b의 값이 짝수인지 홀수인지 파악한다.
# 2. b의 값이 짝수라면 10 ^10 -> (10^5)^2 형태로 바꿔준다.
# 3. b의 값이 홀수라면 10 ^11 -> (10^5)^2 * 10 형태로 바꿔준다.