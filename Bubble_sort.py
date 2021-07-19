def bubble_sort(n,data):
    for i in range(n-1):
        sc=0
        for j in range(n-1):
            if data[j]>data[j+1]:
                sc+=1
                data[j],data[j+1]=data[j+1],data[j]
        print(data,sc)
        if sc==0:
            break
    

n=int(input())
data=list(map(int,input().split()))
bubble_sort(n,data)
