class Student:
    def setMethod(self,name,age,address,rollno):
        self.name=name
        self.age=age
        self.address= address
        self.rollno= rollno
    def getMethod(self):
        print(f"The name of Student is {self.name}, age is {self.age}, address is {self.address} and rollno is {self.rollno}")

e1 =  Student()
e1.setMethod(input("Enter the name of Student"), input("Enter the age"), input("Enter the address"), print("Enter the rollno"))
e1.getMethod()