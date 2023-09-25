class Student:
    def __init__(self,name,age,address):
        self.name= name
        self.age= age
        self.address= address
    def StudentInfo(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"

student = Student("Anjila",22,"Kalanki")
print(student.StudentInfo())
