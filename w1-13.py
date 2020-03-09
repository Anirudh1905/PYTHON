n=int(input())
a=[]
b=[]
c=[]
for i in range(n):
    x=int(input())
    a.append(x)
l=max(a)
a.remove(l)
print(max(a),l)