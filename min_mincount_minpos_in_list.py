def findmin(n,data):
    mi=data[0]
    res=[]
    mic=0
    for i in range(n):
        if data[i]<mi:
            mi=data[i]
            mic=1
        elif data[i]==mi:
            mic+=1    
    #res=[mi,mic]
    res.append(mi)
    res.append(mic)
    for i in range(n):
        if data[i]==mi:
            res.append(i)
    return res
n=int(input())
data=list(map(int,input().split()))
minval=findmin(n,data)
print(*minval)
