class DemoClass: #camel case
    a=10
    def sum(self):
        print(self.a+self.a)
    def show(self):
        print("OOP stands for Object Oriented Programming language")
    def sub(self,a):
        print(a-5)

demoobj=DemoClass()
demoobj.sum()
demoobj.show()
demoobj.sub(11)