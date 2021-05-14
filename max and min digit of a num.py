
''' using Lists '''
n=int(input())
l=list(n)
print("max=",max(l))
print("min=",min(l))


'''using loops'''
n=int(input())
s=9
l=0
while n:
    r=n%10
    n=n//10
    if r>l:
        l=r
    if r<s:
        s=r
print(s,l)

''' or'''
n=int(input())
min=n%10
max=n%10
while n:
    r=n%10
    n=n//10
    if r>max:
        max=r
    if r<min:
        min=r
print(s,l
    
