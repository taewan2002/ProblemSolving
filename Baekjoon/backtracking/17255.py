def dfs(string):
    global cnt
    set_string = set(list(string))
    if len(set_string) == 1:
        cnt+=1
        return cnt
    else:
        dfs(string[1:])
        dfs(string[:-1])

n = input()
cnt = 0
dfs(n)
print(cnt)