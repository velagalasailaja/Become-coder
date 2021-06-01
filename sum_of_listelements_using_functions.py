def sum(n,d):
    res=0
    for i in d:
        res=res+i
    return res

n=int(input())
d=list(map(int,input().split()))
print(sum(n,d))
