#There two type of varible i OOP
#1. Instance Variables
# Variables made for particular instance
# Separate copy is created for every object
# Values of variables differs from object to object

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1 = Student("Anna",12)
s2 = Student("Annie",14)
s3 = Student("Aastha",22)
s1.address= 'Kuleshwor'  #This varible is only for s1 object
print(s1.__dict__)
print(s2.__dict__)

#2. Class Variables and class method
#  Variables ade for entire class(for all object)
#     Only one copy is created and distributed to all objects
# Modification in class varibale impact on all object


class Employee:
    company_name ="Google"
    def __init__(self,name,depart):
        self.name=name
        self.department= depart
e1 = Employee("Abanish","IT")
e2 = Employee("Avash",'HR')
print(Employee.company_name)
print(e1.__dict__)