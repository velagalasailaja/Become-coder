def reverse(n):
    rev=0
    while n:
        r=n%10
        n=n//10
        rev=rev*10+r
    return rev
def find_smin(n,data):
    mi=min(data)
    data[data.index(mi)]=reverse(mi)
    for i in data:
        if i<reverse(mi):
            res=0
        else:
            res=1
    if res==1:
        return 'supermin'
    else:
        return 'Notsupermin'
def find_smax(n,data):
    ma=min(data)
    data[data.index(ma)]=reverse(ma)
    for i in data:
        if i>reverse(ma):
            res=0
        else:
            res=1
    if res==1:
        return 'supermax'
    else:
        return 'Notsupermax'   
n=int(input())
data=list(map(int,input().split()))
smin=find_smin(n,data)
smax=find_smax(n,data)
print(smin,smax)
