n=int(input())
bi=0
c=1
while n:
    r=n%2
    n=n//2
    if r==1:
        r=0
    else:
        r=1
    bi=bi+r*c
    c=c*10
print(bi)
