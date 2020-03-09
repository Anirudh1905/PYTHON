s=input()
c,d=0,0
for k in range(len(s)):
    for i in range(k,len(s)):
        #print(s[k:i+1],end="")
        if(s[k]=="A" or s[k]=="E" or s[k]=="I" or s[k]=="O" or s[k]=="U"):
            c+=1
        else:
            d+=1
if c>d:
    print("Kevin {}".format(c))
elif c<d:
    print("Stuart {}".format(d))
else:
    print("Draw")
