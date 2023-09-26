class Employee:
    def setMethod(self,name,post,salary):
        self.name =name
        self.post= post
        self.salary= salary
    def getMethod(self):
        print(f"The name is {self.name} post is {self.post} and salary is {self.salary}")

e1=Employee()
e2=Employee()

e1.setMethod(input("Enter the name:"),input("Enter the post:"),input("Enter the salary:"))
print(e1.__dict__)
e1.getMethod()