x=input()
t=int(input())
while t!=0:
    z=input()
    c=0
    d=0
    for i in range(4):
        for j in range (4):
            if x[i]==z[j] and i==j:
                c+=1
            elif x[i]==z[j]:
                d+=1
    print(c,d)
    t-=1