n=int(input())
for i in range(n):
    com=int(input())
    wears={}
    for i in range(com):
        a,b=input().split()
        if b in wears:
            wears[b].append(a)
        else:
            wears[b]=[a]
    a=[]
    for key,values in wears.items():
        a.append(len(values)+1)
    
    ans=1
    for i in a:
        ans*=i
    
    print(ans-1)