from operator import itemgetter
n = int(input())
m = int(input())

ar = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        x = int(input())
        ar[i][j] = x
k=int(input())
ar=sorted(ar,key=itemgetter(k))
for i in ar:
    print(*i)
print(ar)
