class Car:

    def setterFun(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price

    def getterFun(self):
        print(f"The name of car is {self.name}, the model is {self.model},the price is{self.price}")

c = Car()
name_car = str(input("Enter the name of car:"))
model_car = str(input("Enter the model of car:"))
price = int (input("The cost of  car is:"))
c.setterFun(name_car,model_car,price)
c.getterFun()
