''' LCM OF 2 NUMBERS '''
'''
t  a      b
2  12     24
-------------
2  12//2  24//2
2   6      12
----------------
3   3      6
-------------2 not diviible by 3 and 6 so increment 2 by 1
    1      2
Lcm=2*2*3*1*2=24
'''
''' Using functions '''
##def lcm(a,b):
##    t=2
##    res=1
##    while True :
##        if a%t==0 and b%t==0:
##            a=a//t
##            b=b//t
##            res=res*t
##        else:
##            t+=1
##        if a<t or b<t:
##            break
##    return (res*a*b)
##a,b=map(int,input().split())
##print(lcm(a,b))

''' using RECUrsion'''
'''
def lcm(a,b,t):
    if a<t or b<t:
        return a*b
    if a%t==0 and b%t==0:
        return t*lcm(a//t,b//t,t)
    else:
        return lcm(a,b,t+1)
a,b=map(int,input().split())
print(lcm(a,b,2))

'''
''' or'''
def lcm(a,b):12,13
    m=max(a,b)
    for i in range(m,






































    
