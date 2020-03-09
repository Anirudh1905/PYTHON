n=int(input())
k=0
t=0
m=0
n=n*2-1
for i in range(1,n+1):
    if n%2==0:
        t=n//2
    else:
        t=(n//2)+1
    if i>t:
        k-=1
    else:
        k+=1
    m=n//2
    for j in range(1,n+1):
        #print(m,end="")
        
        if j<t+1-k or j>t-1+k:
            print("-",end="")
        else:
            if j>=n//2+1:
                print("{}-".format(chr(65+m)),end='')
                m+=1
            else:
                print("{}-".format(chr(65+m)),end='')
                m-=1
    print("\n",end='')