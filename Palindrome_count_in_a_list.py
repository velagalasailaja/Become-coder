def reverse(n):
    rev=0
    while n:
        r=n%10
        n=n//10
        rev=rev*10+r
    return rev
def palicount(n,data):
    palicount=0
    for i in range(n):
        if data[i]==reverse(data[i]):
            palicount+=1
    return palicount        
n=int(input())
data=list(map(int,input().split()))
print(palicount(n,data))

