def secondlargest(n,data):
    s=set(data)
    r=(list(s))
    r.sort()
    return r[-2]

n=int(input())
data=list(map(int,input().split()))
print(secondlargest(n,data))
