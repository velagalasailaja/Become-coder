def is_sorted(data):
    temp1=data.copy()
    temp2=data.copy()
    temp1.sort()
    temp2.sort(reverse=True)
    return (data==temp1 or data==temp2)
data=list(map(int,input().split()))
print(is_sorted(data))
