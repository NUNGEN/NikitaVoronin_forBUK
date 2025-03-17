# class chillguy:
#     def __init__(self,age,hobby,name):
#         self.age = age
#         self.hobby = hobby
#         self.name = name
#         print("Chillguy")
#     def helloGuy(self):
#         print("Hi im just a "+ self.name + " ,my age is " +self.age + " and my hobby is " +self.hobby)
# guy1 = chillguy("16", "workout.","Fjodor Rusanov")
# guy2 = chillguy("16","joging.","Tymur Umanets")
# print(guy1.name)
# print(guy2.name)
# guy1.helloGuy()
# guy2.helloGuy()

class employee:
    self.EMPname = EMPname
    self.EMPwork = EMPwork
    self.EMPage = EMPage
    
class Organization:
    def __init__(self, name, laptops, employee):
        self.name = name
        self.laptops = laptops
        self.employee = employee
#    def employeeinfo(self):
        
class Laptop:
        def __init__(self, brand, ram, storage, year, model):
            self.brand = brand
            self.ram = ram
            self.storage = storage
            self.year = year
            self.model = model
            
        def updateLaptop(self,ramUpdated=0,storageUpdated=0,yearUpdated=0):
            if ramUpdated != 0:
                self.ram = ramUpdated
            if ramUpdated != 0:
                self.storage = storageUpdated
            if ramUpdated != 0:
                self.ram = yearUpdated
            if 2025 -(self.year) >= 5 :
             
        def years(self):
            if 2025 - (self.year) >= 5 :
                print("pc demolition")
        def giveGift(self,organization,laptop):
legion = Laptop("Lenovo",16,512,2012, "XP13")
employee =employee(15,"1000 euros per month","coder")
print(legion.storage)
legion.updateLaptop(ramUpdate=32)
legion.updateGift(afrcia2,legion)

# class Car:
#     #pass
#     def __init__(self,color,engine):
# 
#         self.color = color
#         self.engine = engine
#         print("autode loomine")
#         
#     def helloSayer(self):
#         print("hello you have" + self.color + " bmw")
# bmw = Car("Black","bensiin")
# bmw2 = Car("Green","electer")
# print(bmw.color)
# print(bmw2.color)
# bmw.helloSayer()
