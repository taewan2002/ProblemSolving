n = int(input())
p = 1000000007

# n번 째 피보나치 수는 행렬 (1 1, 1 0)^n 의 1행 2열 값이다(단, n>=1일때)

def mul(A, B):
    n = len(A)
    new_matrix = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += A[row][i] * B[i][col] # 행렬 곱셈
            new_matrix[row][col] = e % p # 행렬 곱셈의 결과를 p로 나눈 나머지
            
    return new_matrix

def square(fib_matrix, k):
    if k == 1:
        for x in range(len(fib_matrix)):
            for y in range(len(fib_matrix)):
                fib_matrix[x][y] %= p 
        return fib_matrix 
    
    tmp = square(fib_matrix, k//2) # k//2번째 피보나치 수의 행렬
    if k % 2: # 홀수
        return mul(mul(tmp, tmp), fib_matrix) # (A^2) * A
    else: # 짝수
        return mul(tmp, tmp) # A^2
    
fib_matrix = [[1, 1], [1, 0]] # 피보나치 수의 행렬
print(square(fib_matrix, n)[0][1]) # n번째 피보나치 수의 행렬의 1행 2열 값

# https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-11444-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%88%98-6-%EA%B3%A8%EB%93%9C3-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5