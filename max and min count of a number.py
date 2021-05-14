n=int(input())
ma=n%10
mi=n%10
temp=n
mic=0
mac=0
while n:
    r=n%10
    n=n//10
    if r>ma:
        ma=r
    if r<mi:
        mi=r
print(ma,mi)
while temp:
    r=temp%10
    temp=temp//10
    if ma==r:
        mac+=1
    if mi==r:
        mic+=1
print(mac,mic)



