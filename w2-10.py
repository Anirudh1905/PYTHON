n=int(input())
k=int(input())
a=[]
for i in range(0,n):
    a.append(int(i+1))
c=1
i=0
while len(a)!=1:
    i=i%len(a)
    if c%k==0:
        a.remove(a[i])
        c=0
    else:
        i+=1
    c+=1
print(a)   