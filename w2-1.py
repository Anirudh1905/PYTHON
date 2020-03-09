n=int(input())
a=[]
for i in range(n):
    x=int(input())
    a.append(x)
d=int(input())
m=int(input())
c=0
j=0
for i in range(n):
    s=0
    l=0
    j=i
    while(l!=m and j<n):
        
        s=s+a[j]
        l+=1
        j+=1
        
    if s==d:
        c+=1
print(c)