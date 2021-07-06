"""Normal method """
##data=list(map(int,input().split()))
##key=int(input())
##for i in data:
##    if key==i:
##        print("Found")
##        break
##else:
##    print("Not Found")
    
''' using functions '''
##def Linearsearch(data,key):
##    for i in data:
##        if key==i:
##            return True
##    return False
##data=list(map(int,input().split()))
##key=int(input())

""" using OOPS """
class search:
    def __init__(self,n,data,key):
        self.n=n
        self.data=data
        self.key=key
    def linearsearch(self):
        for i in self.data:
            if self.key==i:
                return True
        return False
n=int(input())
data=list(map(int,input().split()))
key=int(input())
s1=search(n,data,key)
print(s1.linearsearch())






    
