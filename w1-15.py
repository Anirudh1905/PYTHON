x=int(input())
a=[]
a.append(2)
f=0
for i in range(3,x//2):
    for j in range(2,(i//2)+1):
        if i%j==0:
            f=1
    if f==0:
        a.append(i)
    f=0
for i in a:
    while x%i==0:
        print("{} ".format(i),end="")
        x=x/i