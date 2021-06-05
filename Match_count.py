def org(n,data):
    l=[]
    for i in data:
        if i  not in l:
            l.append(i)
    return l
n=int(input())
data=list(map(int,input().split()))
d=org(n,data)
print(*d)
c=0
for i in range(len(d):
    if data[i]==d[i]:
        c+=1
print(c)
    
