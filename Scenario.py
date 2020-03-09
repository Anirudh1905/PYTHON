class customer:
    a=[]
    b=[]
    def input(self):
        self.s=input("enter your name")
        self.n=int(input("enter no. of items"))
        for self.i in range(self.n):
            self.z=input("enter {} item name".format(self.i+1))
            self.b.append(self.z)
            self.t=int(input("enter {} item price".format(self.i+1)))
            self.a.append(self.t)
class shopkeeper(customer):
    def calculation(self):
        self.x=sum(self.a)
        if self.x>=5000:
            self.x=self.x-self.x/10
    def disp(self):
        print("Customer Name: {}".format(self.s))
        for self.i in range(0,self.n,1):
            print("{} {}          price {}".format(self.i+1,self.b[self.i],self.a[self.i]))
        print("Total bill: {}".format(self.x))
q=int(input("enter no. of customer"))
for i in range(q):
    obj=shopkeeper()
    obj.input()
    obj.calculation()
    obj.disp()
        