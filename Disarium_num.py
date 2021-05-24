def is_disarium(n):
    c=0
    temp=n
    s=0
    
    while n:
        n=n//10
        c+=1
    n=temp
    while n:
        r=n%10
        n=n//10
        s=s+pow(r,c)
        c-=1
    return s==temp
n=int(input())
print(is_disarium(n))
        

