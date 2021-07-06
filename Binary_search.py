''' Normal method '''
##n=int(input())
##data=list(map(int,input().split()))
##key=int(input())
##data.sort()
##L,H=0,n-1
##while L<=H:
##    m=(L+H)//2
##    if key==data[m]:
##        print("Found")
##        break
##    elif key<data[m]:
##        H=m-1
##    else:
##        L=m+1
##else:
##    print("Not Found")

''' Using Functions '''
##def binarysearch(n,data,key):
##    data.sort()
##    L,H=0,n-1
##    while L<=H:
##        m=(L+H)//2
##        if key==data[m]:
##            return True
##        elif key<data[m]:
##            H=m-1
##        else:
##            L=m+1
##    return False
##n=int(input())
##data=list(map(int,input().split()))
##key=int(input())
''' using  oops'''
class search:
    def __init__(self,n,data,key):
        self.n=n
        self.data=data
        self.key=key
    def binarysearch(self):
        self.data.sort()
        L,H=0,n-1
        while L<=H:
            m=(L+H)//2
            if self.key==self.data[m]:
                return True
            elif self.key<self.data[m]:
                H=m-1
            else:
                L=m+1
        return False
n=int(input())
data=list(map(int,input().split()))
key=int(input())
s1=search(n,data,key)
print(s1.binarysearch())

        


        
            
        
        
