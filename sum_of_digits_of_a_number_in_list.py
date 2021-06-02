def res(n):
    s=0
    while n:
        r=n%10
        n=n//10
        s+=r
    return s
def sumofdigits(n,d):
    for i in range(n):
        d[i]=res(d[i])

n=int(input())
d=list(map(int,input().split()))
sumofdigits(n,d)
print(*d)
