def reverse(n):
    rev=0
    while n:
        r=n%10
        n=n//10
        rev=rev*10+r
    return rev
def find_smin(n,data):
    mi=min(data)
    r=reverse(mi)
    data[data.index(mi)]=r
    mi1=min(data)
    return r==mi1   
def find_smax(n,temp):
    ma=max(temp)
    r=reverse(ma)
    temp[temp.index(ma)]=r
    ma1=max(temp)
    return r==ma1    
n=int(input())
data=list(map(int,input().split()))
temp=data.copy()
smin=find_smin(n,data)
smax=find_smax(n,temp)
print(smin,smax)
