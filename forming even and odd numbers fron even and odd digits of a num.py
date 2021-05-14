n=int(input())
even,odd=0
ec=oc=1
while n:
    r=n%10
    n=n//10
    if r%2==0:
        even=even+r*ec
        ec=ec*10
    else:
        odd=odd+r*oc
        oc=oc*10
print(even,odd)
