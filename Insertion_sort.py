def insertion_sort(n,data):
    for i in range(1,n):
        key=data[i]
        for j in range(i-1,-1,-1):
            if key>data[j]:
                data[j+1]=key
                break
            else:
                data[j+1]=data[j]
            
        else:
            data[0]=key
        print(data)        
n=int(input())
data=list(map(int,input().split()))
insertion_sort(n,data)
'''
9
88 14 22 55 41 99 44 10 34
[14, 88, 22, 55, 41, 99, 44, 10, 34]
[14, 22, 88, 55, 41, 99, 44, 10, 34]
[14, 22, 55, 88, 41, 99, 44, 10, 34]
[14, 22, 41, 55, 88, 99, 44, 10, 34]
[14, 22, 41, 55, 88, 99, 44, 10, 34]
[14, 22, 41, 44, 55, 88, 99, 10, 34]
[10, 14, 22, 41, 44, 55, 88, 99, 34]
[10, 14, 22, 34, 41, 44, 55, 88, 99]
'''
































