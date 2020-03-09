a=[]
for i in range(5):
    x=int(input())
    a.append(x)
x=min(a)
a.remove(x)
print(sum(a))
a.append(x)
a.remove(max(a))
print(sum(a))
