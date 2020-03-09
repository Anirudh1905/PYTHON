from fractions import Fraction
import functools 
a=[]
n=int(input())
for i in range(n):
    x=int(input())
    y=int(input())
    a.append(Fraction(x,y))
t=functools.reduce(lambda c,d : c*d,a)
print("{} {}".format(t.numerator,t.denominator))

