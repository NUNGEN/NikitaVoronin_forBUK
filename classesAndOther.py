# class Patient:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# 
# class Doctor:
#     def __init__(self,name,age,profession,time):
#         self.name = name
#         self.age = age
#         self.profession = profession
#         self.time = time
#     
# class Durka:
#     def __init__(self):
#         self.patientlist = []
#         self.doctorlist = []
#         self.registration = []
#         
#     def showDoctors(self):
#         for elem in self.doctorlist:
#             print("Doctor name: ",elem.name,"age:",elem.age, "profession",elem.profession)
#             if len(elem.aeg)>0:
#                 print("Doctor is active for time: ")
#                 for time in self.time:
#                     print(time)
#                     
#     def showRecords(self):
#         print("Records in Durka")
#         print("----------------------------")
#         
#     def visitDoctor(self,doctor):
#         visitedDoctorName = input("input doctor's name")
#         for elem in self.doctorlist:
#             if visitedDoctorName == elem.nimi:
#                 self.showDoctors(elem)
#                 userInput = input("Which time do you prefer ?")
#                 
#                 if userInput in elem.time:
#                     elem.time.remove(userinput)
#                 else:
#                     print("units were given incorrectly")
#         
#             
#     def showPatients(self):
#         for elem in self.doctorlist:
#             print("id: ", index, "Patient name:",elem.name,"age",elem.age )
# 
# patient1 = Patient("Thomas", 88)
# patient2 = Patient("Adun", 30)
# doctor1 = Doctor("Faust",45,"Surgeon",['9:00','10:00','20:31'])
# doctor2 = Doctor("Fedor",18,"Urologist",['3:00','4:00','4:20'])
# doctor3 = Doctor("Fanny",24,"Nurse",['9:00','12:12','21:31'])
# durka = Durka()
# 
# durka.doctorlist.append(doctor1)
# durka.doctorlist.append(doctor2)
# durka.doctorlist.append(doctor3)
# durka.registration.append(Doctor)

# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("drive!")
#         
# class Boat:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Sail!")
#         
# class Plane:
#      def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Fly!")
#     
# car1 = Car("Ford","Mustang")
# boat1 = Boat("Ibiza","Touring 20")
# plane1 = Plane("Boeing","747")
# 
# for i in [car1,boat1,plane1]:
#     i.move()
    
#  Lion,Monkey,Elephant,Penguin
#  eat()
#  makeSound()

class Lion:
    def __init__(self,eat,makeSound):
         self.brand = brand
         self.model = model
     def move(self):
         print()
         print("Rarrw !!")
         
class Monkey:
        def __init__(self,eat,makeSound):
         self.brand = brand
         self.model = model
     def move(self):
         print()
         print("Uaau-uaaau-ua-aaa-a-a")
class Elephant:
    def __init__(self,eat,makeSound):
         self.brand = brand
         self.model = model
     def move(self):
         print()
         print("Uuuuuff")
class Penguin:
    def __init__(self,eat,makeSound):
         self.brand = brand
         self.model = model
     def move(self):
         print()
         print("Shhhiihhh-a-a-aa")
    
    