def min_max(n,data):
    mi=data[0]
    ma=data[0]
    for i in range(n):
        if data[i]<mi:
            mi=data[i]
        elif
        if data[i]>ma:
            ma=data[i]
    return mi,ma    
n=int(input())
data=list(map(int,input().split()))
mi,ma=min_max(n,data)
print(mi,ma)
    
