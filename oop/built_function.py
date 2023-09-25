#getattr()
#setattr()
#deleteattr()
#hasattr()

class Employee:
    def __init__(self,name,address):
        self.name = name
        self.address = address

e1 = Employee('Anjila','Kalanki')
e2= Employee('Maya','Bagbazar')
e3= Employee('Shreya','Kalamti')
print(getattr(e1,'address'))
(setattr(e2,'name','Mann'))
print(e2.__dict__)
delattr(e3,'address')
print(e3.__dict__)
print(hasattr('e3','address'))
