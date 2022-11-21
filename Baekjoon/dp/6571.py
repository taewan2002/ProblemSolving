while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0: break
    cnt = 0
    dp = [] 
    dp.append(1)
    dp.append(2)
    while True:
        dp.append(dp[-1] + dp[-2])
        if dp[-1] >= b: break
    for i in dp:
        if a <= i <= b: 
            cnt += 1
    print(cnt)