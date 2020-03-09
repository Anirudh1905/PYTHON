s=input()
n=len(s)
k=int(input())
t=n//k
c=0
j=0
p=""
x=k
l=0
for i in range(t):
    s1=s[j:x]
    p=s1[0]
    for l in range(1,k):
        if(p.find(s1[l])==-1):
            p=p+s1[l]
    print(p)    
    p=""
    s1=""
    j+=k
    x+=k
