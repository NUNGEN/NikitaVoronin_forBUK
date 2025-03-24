# class Person:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
#         
#     def print_person(self):
#         print(self.__name, self.__age)
#     @property   
#     def get_name(self):
#         return self.name
#     @age.setter
#     def set_age(self,age):
#         if age<0:
#             print("Error: age does'not match")
#         self.__age = age
#         
# tom = Person("Tom", 39)
# tom.__name = "Jerry"
# tom.print_person()
# tom.set_age(40)
# tom.print_person()

# class Student:
#     def __init__(self,name):
#         self.name = name
#         self.__grades = [5,4,3,5,5,4]
#     
#     def get_grades(self):
#         return self.__grades
#     
#     def add_grade(self, grade):
#         self.__grades.append(grade)
#         
#     def displayInfo(self):
#         print("name: ", self.name,self.__grades)
#     def averaga(self)
#         result sum(avg)
#             return sum(grades) / len(grades)
#     
# avg =[5,4,3,5,5,4]
# superStudent = Student("SuperSus")
# superStudent.displayInfo()
# superStudent.add_grade(5)
# superStudent.displayInfo()
# #print(superStudent.name)
# 
# class Course:
# 
#     def __init__(self,title):
#         if isinstance(students, Student)
#             self.__students = []
#         else:
#             print("Do not input other people")
#         
# superStudent
# superStudent = Student("SuperSus")
# superStudent.displayInfo()
# superStudent.add_grade(5)
# superStudent.displayInfo()
# print(superStudent.name)
# 
# class Animal:
#     def __init__(self,name,paws,eyes,tail,has_fur):
#         self.paws = paws
#         self.eyes = eyes
#         self.tail = tail
# class Mammal(Animal):
#     def __init__(self,name,paws,eyes,tail,has_fur):
#         super().__init__(name,paws,eyes,tail,has_fur)
#         self.name = name
#         self.has_fur = has_fur
#         
#     def speak(self):
#         print(self.name,"- imetaja")
#     
# class Dogs(Mammal):
#     def __init__(self,name,paws,eyes,tail,has_fur,breed):
#         super().__init__(name,paws,eyes,tail,has_fur)
#         self.breed = breed
#         
#     def speak(self):
#         print("bark bark")
# #self.nickname = nickname
# pes = Dogs('Dog',4,2,1,True,'Sharik')
# #print(pes.breed)
# pes.speak()

class Vehicle:
    def __init__(self,brand,vehicle_type,model):
        self.brand = brand
        self.vehicle_type = vehicle_type
        self.model = model
class Car(vehicle)
    def __init__(self,brand,vehicle_type,model,fuel_type):
        super()__init__(brand,vehicle_type,model)
        self.fuel_type = fuel_type
class Electrocar(car)
    def __init__(self,brand,vehicle_type,model,fuel_type,battery_charge):
        super()__init__(brand,vehicle_type,model,fuel_type)
        self.battery_charge = battery_charge
car = car("")

