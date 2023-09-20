class Student:
    def __init__(self):
        self.name=""
    def get(self):
        return self.name
    def set(self,name):
        self.name=name
obj=Student()
obj.set("Anjilaaaa")
name = obj.get()
print(name)
