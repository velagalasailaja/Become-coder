''' method 1--ascending order'''
##def selection_sort(n,d):
##    for i in range(n-1):
##        if i==0:
##            m=max(d)
##            d[d.index(m)],d[-1]=d[-1],d[d.index(m)]
##            print('p'+str(i+1)+':',d)
##        else:
##            m=max(d[:-i])
##            d[d.index(m)],d[-i-1]=d[-i-1],d[d.index(m)]
##            print('p'+str(i+1)+':',d)
##n=int(input())
##data=list(map(int,input().split()))
##selection_sort(n,data)
##print(*data)

''' or'''

##def selection_sort(n,d):
##    m=max(d)
##    for i in range(1,n):
##        d[-i],d[d.index(m)]=d[d.index(m)],d[-i]
##        m=max(d[:-i])
##        print(d)
##n=int(input())
##data=list(map(int,input().split()))
##selection_sort(n,data)

''' method 2 --Ascending order'''
##def selection_sort(n,d):
##    m=min(d)
##    for i in range(0,n-1):#i=0-n-1
##        d[d.index(m)],d[i]=d[i],d[d.index(m)]
##        m=min(d[i+1:])
##        print('pass'+str(i+1)+':',d)           
##n=int(input())
##data=list(map(int,input().split()))
##selection_sort(n,data)

''' method 3--Descending order'''

##def selection_sort(n,d):
##    m=max(d)
##    for i in range(0,n-1):
##        d[d.index(m)],d[i]=d[i],d[d.index(m)]
##        m=max(d[i+1:])
##        print('pass'+str(i+1)+':',d)
##        
##n=int(input())
##data=list(map(int,input().split()))
##selection_sort(n,data)

''' method 4---Descending order'''
def selection_sort(n,d):
    m=min(d)
    for i in range(1,n):
        d[d.index(m)],d[-i]=d[-i],d[d.index(m)]
        m=min(d[:-i])    
        print(d)
n=int(input())
data=list(map(int,input().split()))
selection_sort(n,data)






















