# Create Parent Class called Car - That will be inherited by child Class called Ford
# Add a method to the Car class that prints "This is a car"
# Inside of the Child Class initialize the the inherited info using super()
# Override the above method with the information of the Ford Car

class Car():
    def __init__(self, make, model, wheel=4):
        self.make = make
        self.model = model
        self.wheel = wheel

    def carType(self):
        return f"This is a car and it's a {self.make} {self.model}"


class Ford(Car):
    def __init__(self, make, model, wheel, color='white'):
        super().__init__(make, model, wheel)
        self.color = color

    def carType(self):
        return f"This {self.make} {self.model} is better though!"
    
generic_car = Car('Ford', 'Focus')
print(generic_car.carType())

fordExplorer = Ford('Ford', 'Explorer', 4)
print(fordExplorer.carType())