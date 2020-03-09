n=int(input())
a=[]
b=[]
c=[]
for i in range(n):
    x=int(input())
    a.append(x)
print(a)
for i in range(n):
    if a[i]%2==0:
        b.append(a[i])
    else:
        c.append(a[i])
print(b,c)