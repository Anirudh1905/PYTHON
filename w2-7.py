a=[]
n=int(input())
for i in range(n):
    x=int(input())
    a.append(x)
k=0
for i in range(n):
    if i+2<n:
        if a[i]==0 and a[i+2]==0:
            k+=1
            i+=1
    elif i+1<n:
        if a[i]==0 and a[i+1]==0:
            k+=1
print(k)
    