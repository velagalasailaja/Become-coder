def movezeros(n,arr):
    d=arr.count(0)
    for i in range(d+1):
        arr.remove(0)
        arr.append(0)
n=int(input())
arr=list(map(int,input().split()))
movezeros(n,arr)
print(*arr)
