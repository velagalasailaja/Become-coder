def count(n,data):
    ec=0
    oc=0
    for i in data:
        if i%2==0:
            ec+=1
        else:
            oc+=1
    return ec,oc

n=int(input())
data=list(map(int,input().split()))
res=count(n,data)
print(*res)
