class Person:

    def __init__(self,name,address):
        self.name=name
        self.address= address
    def info(self):
        print(f"Name is{self.name}, Address is{self.address}")

class Employee(Person):
    pass

e1 = Employee('Ram','Birjung')
e1.info()