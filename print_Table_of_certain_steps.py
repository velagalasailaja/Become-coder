'''using for loop'''
n,r=map(int,input().split())
for i in range(1,r+1):
    print(n,"x",i,"=",n*i)
'''using while loop'''
n,r=map(int,input().split())
i=1
while i<=r:
    print(n,"x",i,"=",n*i)
    i+=1
    
