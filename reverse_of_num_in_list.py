def reverse(n):
    rev=0
    while n:
        r=n%10
        n=n//10
        rev=rev*10+r
    return rev
def revlist(n,data):
    for i in range(n):
        data[i]=reverse(data[i])
        
n=int(input())
data=list(map(int,input().split()))
revlist(n,data)
print(*data)
