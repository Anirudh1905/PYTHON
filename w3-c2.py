
import math
class Tor(object):
	def __init__(self,x,y,z):
    	self.x=x
    	self.y=y
    	self.z=z
	def __sub__(self,no):
    	return Tor(self.x-no.x,self.y-no.y,self.z-no.z)
	
	def dot(self, no):
    	return (self.x*no.x)+(self.y*no.y)+(self.z*no.z)
	def cross(self, no):
    	return Tor((self.y*no.z-self.z*no.y),(self.z*no.x-self.x*no.z),(self.x*no.y-self.y*no.x))
    	
	def absolute(self):
    	return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
points=[]
for i in range(4):
	q=list(map(float,input().split()))
	points.append(q)
a,b,c,d=Tor(*points[0]),Tor(*points[1]),Tor(*points[2]),Tor(*points[3])
x=(b-a).cross(c-b)
y=(c-b).cross(d-c)
angle=math.acos(x.dot(y)/(x.absolute()*y.absolute()))
print("%.2f"% math.degrees(angle))
