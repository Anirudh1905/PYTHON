a=[]
b=[]
n=int(input())
for i in range(n):
    x=int(input())
    a.append(x)
b.append(len(a))
q=0
i=0
while len(a)!=0:
    l=min(a)
    i=0
    while i<len(a):
        a[i]-=l
        if a[i]==0:
            a.remove(a[i])
            continue
        i+=1
    if len(a)==0:
        break
    b.append(len(a))
print(b)
