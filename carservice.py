class CarPark(name):
    def __init__(self,):

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        self.year = year
        self.broken = False
    def breakDown(self):
        self.broken = True
#class Service
        
class ServiceCenter(name):
    def __init__(self,name):
        self.name = name
        
    def carRepair(self,Car):
        Car.broken = False
        
class Owner(name):
    def __init__(self,name):
        self.name = name
        self.cars = []
        
    def addCars(self,car):
#        print(car)
        self.cars.append(car)
        
    def CarsToServiceCenter(self,ServiceCenter):
        print("Kasutja saatis reemondikeskusse sellised autod:")
        for Car in self.cars:
            if Car.broken:
                Car.displayInfo()
                serviceCenter.carRepair(Car)
                
carCenter = ServiceCenter("ServiceCenter")

class Invoice()

car1 = Car("BMW","E34",1997)
car.broken = True
car2 = Car("Ferrari","Roma",2024)
car.broken = True
car3 = Car("Tesla","Model 3",2016)
car4 = Car("Toyota","Corolla",2020)

MarkZuckenberg = Owner("Mark Zuckenberg")
MarkZuckenberg.CarsToServiceCenter
MarkZuckenberg.addCars(car1)
MarkZuckenberg.addCars(car2)
MarkZuckenberg.addCars(car3)
MarkZuckenberg.addCars(car4)
MarkZuckenberg.sendCarsToServiceCenter(carCenter)

car1.broken = True
carCenter.carRepair(car1)
print(car1.broken)
