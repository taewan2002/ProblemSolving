p = int(input())

for i in range(p):
    n, m = map(int, input().split())
    fibo = [0, 1, 1]
    while True:
        fibo.append((fibo[-1] + fibo[-2])%m)
        if fibo[-1] == 1 and fibo[-2] == 0:
            break
        
    print(f"{i+1} {len(fibo)-2}")
    
# 피사노 주기 구하기