# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 21:19:13 2020

@author: aniru
"""

n=int(input())
k=0
t=0
for i in range(1,n+1):
    if n%2==0:
        t=n//2
    else:
        t=(n//2)+1
    for j in range(1,n+1):
        if j==t-i+1 or j==t+i-1 or i==t and j>1 and j<n or i>t and (j==1 or j==n):
           print("*",end="")
        else:
            print(" ",end='')
    print("\n",end='')