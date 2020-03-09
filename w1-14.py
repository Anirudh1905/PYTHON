a=[]
for i in range(100,1001):
    a.append(i)
e=list(filter(lambda n:n%5==0 and n%6==0,a))
c=0
for x in e:
    if c%10==0:
        print("\n")
    else:
        print("{} ".format(x),end="")
    c+=1