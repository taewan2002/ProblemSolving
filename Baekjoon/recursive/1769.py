def recursive(n, cnt):
    if len(n) == 1:
        if int(n) % 3 == 0:
            print(cnt)
            print("YES")
            return
        else:
            print(cnt)
            print("NO")
            return
    total = 0
    for i in n:
        total += int(i)
    recursive(str(total), cnt+1)



n = input()
recursive(n, 0)

# Compare this snippet from Baekjoon/backtracking/17256.py:
