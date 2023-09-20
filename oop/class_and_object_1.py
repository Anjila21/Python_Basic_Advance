class Car:
    def __init__(self,name,model,price):
        self.name=name
        self.model = model
        self.price=price

    def manufacture(self):
        print(f"The name of Car is{self.name},which is of{self.model}model and price is Rs.{self.price}")

car = Car('Thar',12567,2700000)
print(car.manufacture())