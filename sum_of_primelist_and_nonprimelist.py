import math as m
def isprime(n):
    if n==1:
        return 0
    s=int(m.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return 0
    return 1
def findprimes(n,data):
    pl=[]
    npl=[]
    for i in data:
        if isprime(i):
            pl.append(i)
        else:
            npl.append(i)
    return pl,npl
n=int(input())
d=list(map(int,input().split()))
primes,np=findprimes(n,d)#primelist,nonprimelist
print(sum(primes))
print(sum(np))
