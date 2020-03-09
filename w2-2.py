n=int(input())
a=[]
b=[]
max1=-100
for i in range(n):
    x=int(input())
    a.append(x)
a.sort()
for i in range(n):
    l=a.count(a[i])
    b.append(l)
for i in range(n):
    if b[i]>max1:
        max1=b[i]
        j=i
print(a[j])