n=int(input())
a=[]
b=[]
max1=-100
for i in range(n):
    x=int(input())
    a.append(x)
i,j
c=0
d=0
for i in range(n):
    if a[i]<=0:
        c+=1;
    elif a[i]>0:
        d+=1;
if c>=k: print("NO");
else: print("YES");