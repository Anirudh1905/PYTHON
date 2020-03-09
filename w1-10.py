n=int(input())
a=[]
b=[]
c=0
d=0
for i in range(n):
    x=int(input())
    if x<0:
        c+=1
    elif x>0:
        d+=1
    a.append(x)
print(c,d)
print(sum(a)/n)