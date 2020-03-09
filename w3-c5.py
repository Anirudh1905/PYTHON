class Queue:
	a=[]
	def __init___(self):
    	r=0
	def insert(self,x):
    	self.a.append(x)
	def remove(self):
    	if len(self.a)==0:
        	print("QUEUE IS EMPTY")
    	else:
        	self.a.pop(0)
	def display(self):
    	for k in self.a:
        	print(k)
ob=Queue()
ob.insert(10)
ob.insert(20)
ob.insert(30)
ob.insert(40)
ob.insert(50)
ob.remove()
ob.display()
