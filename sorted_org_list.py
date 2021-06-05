def sort_org_list(n,data):
        d=list(set(data))
        d.sort()
        return d
n=int(input())
data=list(map(int,input().split()))
res=sort_org_list(n,data)
print(*res)
c=0
for i in range(len(res)):
    if data[i]==res[i]:
        c+=1
print(c)
    

