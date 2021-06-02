import math as m
def countprime(n,data):
    def isprime(n):
        if n==1:
            return 0
        s=int(m.sqrt(n))
        for i in range(2,s+1):
            if n%i==0:
                return 0
        return 1
    for i in data: 
        pc=0
        if isprime(i):
            pc+=1
    return pc
n=int(input())
data=list(map(int,input().split()))
pc=countprime(n,data)
print(pc)
                
                
                
