num=int(input())
count=0
temp1=num
temp2=num
while num:
    num=num//10
    count+=1
##print("No of digits=",count)
res=0
while temp1:
    r=temp1%10
    temp1=temp1//10
    res=res+pow(r,count)
if res==temp2:
    print("ARMSTRONG NUMBER")
else:
    print("NOT ARMSTRONG NUMBER")
