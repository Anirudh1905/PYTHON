# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:31:39 2020

@author: anirudh
"""

x=input()
y=int(x[::-1])
a=[];t=0;d=[];
sr=''
for i in range(len(x)):
    a.append(int(x[i]))
if sorted(a,reverse=True)==a:
    print("not possible")
else:
    for i in range(len(x)-1,-1,-1):
        for j in range(i-1,-1,-1):
            if a[i]>a[j]:
                t=j
                a[i],a[j]=a[j],a[i]
                break
        if t!=0:
            break
    d=a[:t+1]+sorted(a[t+1:])
    for x in d:
        sr=sr+str(x)
    print(sr)
    