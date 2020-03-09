class Number:
	Mul=1
	a=()
	s=[]
	def __init__(self,x,y):
    	self.x=x
    	self.y=y
	def add(self):
    	return self.x+self.y
	def multiply(self,a):
    	return self.Mul*a
	@staticmethod
	def sub(b,c):
    	return b-c
	def value(self):
    	
    	def set1(self,q):
        	self.x=q
    	def det(self):
        	del self.x
    	#self.a=tuple(self.s)
    	self.s.append(self.x)
    	self.s.append(self.y)
    	
    	return self.s
ob=Number(5,6)
print(ob.add())
print(ob.multiply(7))
print(ob.sub(8,2))
print(ob.value().set1(3))
	

