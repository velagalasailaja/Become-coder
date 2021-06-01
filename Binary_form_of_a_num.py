n=int(input())
c=1
bi=0
count=0
while n:
    r=n%2
    n=n//2
    bi=bi+r*c
    c=c*10
print(bi)



