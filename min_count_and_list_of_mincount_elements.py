def min_digit_count(n,data):
    count=[]
    for i in data:
        c=data.count(i)
        count.append(c)
    mc=min(count)
    res=[]
    for i in data:
        if data.count(i)==mc:
            if i not in res:
                res.append(i)
    return mc,res
n=int(input())
data=list(map(int,input().split()))
mc,result=min_digit_count(n,data)
print(mc)
print(*result)
