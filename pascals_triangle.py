#Pascals Triangle
a=[1,2,1]
n=int(input("Enter n:"))
c=n-1
print(c*' ',1)
print((c-1)*' ',1,1)
print((c-2)*' ',1,2,1)
c=n-4
d=[1,2,1]
for i in range(3,n):
    print(c*' ','1',end=' ')
    f=[1]
    e=0
    for i in range(2,i+1):
        print(d[e]+d[e+1],end=' ')
        f.append(d[e]+d[e+1])
        e=e+1
    f.append(1)
    d=f
    c-=1
    print(1)