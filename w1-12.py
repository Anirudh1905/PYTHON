f=open("anil.txt",'r')
x=f.readline()
a=[]
q=x.split(' ')
for e in q:
    y=int(e)
    a.append(y)
print(max(a))