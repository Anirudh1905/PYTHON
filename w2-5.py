n=int(input())
m=int(input())
s=int(input())
if (m+s-1)%n==0:
    print(n)
else:
    print((m+s-1)%n)