s=input()
data=s.split()
n=len(data)
for i in range(n):
    w=data[i]
    print(w[::-1],end=' ')
    
