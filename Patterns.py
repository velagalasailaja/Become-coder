''' Patterns '''
#1.
'''
*****
*****
*****
*****
*****
'''
##
##n=int(input())
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        print('*',end='')
##    print()

#2.
'''
12345
12345
12345
12345
12345
'''
##n=int(input())
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        print(j,end='')
##    print()

#3.
'''
11111
22222
33333
44444
55555
'''
##n=int(input())
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        print(i,end='')
##    print()

#4.
'''
23456
34567
45678
56789
678910
'''
##n=int(input())
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        print(i+j,end='')
##    print()

#4.
'''
54321
54321
54321
54321
54321
'''
##n=int(input())
##for i in range(n,0,-1):
##    for j in range(n,0,-1):
##        print(j,end='')
##    print()

#5.
'''
12345
54321
12345
54321
12345
'''
##n=int(input())
##for i in range(n,0,-1):
##    if i%2==0:
##        for j in range(n,0,-1):
##            print(j,end='')
##    else:
##        for j in range(1,n+1):
##            print(j,end='')
##    print()

#6.
'''
11111
12345
33333
12345
55555
'''
##n=int(input())
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i%2==0:
##            print(j,end='')
##        else:
##            print(i,end='')
##    print()

#7.
'''
12345
22345
32345
42345
52345
'''
##n=int(input())
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if j==1:
##            print(i,end='')
##        else:
##            print(j,end='')
##    print()

#8.
'''
54321
22222
54321
44444
54321
'''
##n=int(input())
##for i in range(1,n+1):
##    if i%2==0:
##        for j in range(1,n+1):
##            print(i,end='')
##    else:
##        for j in range(n,0,-1):
##            print(j,end='')
##    print()

#9.
'''
10101
10101
10101
10101
10101
'''
##n=int(input())
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if j%2:
##            print(1,end='')
##        else:
##            print(0,end='')
##    print()

#10.
'''
10101
01010
10101
01010
10101
'''
##n=int(input())
##for i in range(1,n+1):
##    if i%2==0:
##        temp=0
##    else:
##        temp=1
##    for j in range(1,n+1):
##        print(temp,end='')
##        if temp==0:
##            temp=1
##        else:
##            temp=0
##    print()


















    






    
        
    
