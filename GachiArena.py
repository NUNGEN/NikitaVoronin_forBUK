import random
from abc import ABC, abstractmethod


class PotentialWarriour(ABC):
    def init(self, name, strenght):
        self.name = name
        self.strenght = strenght
        
    @abstractmethod
    def speak(self):
        pass


class Villager(PotentialWarriour):
    def init(self, name, strenght):
        super().init(name, strenght)
        if random.choice == True: # в классе крестьянин выбирается воин через рандомный выбор
            print("Warriour chose to take a part in your legion") 
        else:
            print("Villager denied your offer")
            
    def speak(self):
        print(f"{self.name}: Stays silent")
        
        
class Gladiator(PotentialWarriour): # В дополнение к вербовке крестьянина происходит его выбор в легион. По таким значениям как "сила"
    def init(self, name, strength): # крестьянина и вместимость легиона (вместимоть работает так, что если при вербовке вышло ровно 10
        super().init(name, strength) # то значение не растёт).
        self.legion = []  # Оно также не растёт, если собрали уже больше лимита в 10
    
    def speak(self):
        print("{self.name} BATTLE CRY !")
        
    def recruit(self, villager):
        if len(self.legion) >= 10:
            return
        if villager.ready_to_join and self.strength >= 5:
            self.legion.append(villager)
            
    def demonstrate_legion(self):
        print("My name is Legion: ")
        for i in self.legion:
            print(f"- {i.name}, strenght: {i.strength}")
    
    def legion_training(self):
     for i in self.legion:
            i.strength += 2
            
# class WholeVillages(self):
#     def village(self, name, villages):
#         self.villager_list = [
#             ("Billie", 12),
#             ("Leonid", 8),
#             ("IVan", 6),
#             ("Ricardo", 8),
#             ("Fedor", 6),
#             ("Hikan", 3)
#             ("Spartak", 10),
#             ("Faust", 9),
#             ("Testament", 4),
#             ("Lacksimus", 3),
#             ("Papich", 2),
#             ("Loggame", 1),
# ]
#     
#     villages = [
#     create_village("Gachivanovo", random.int(f"{villager_list}"(3,5)), ),
#     create_village("Shy Hills", random.int(f"{villager_list}"(3,5)), ),
#     create_village("Azafur", random.int(f"{villager_list}"(3,5)), ),
# ]
    def create_village(name_prefix, count):
        return [Peasant(f"{name_prefix}_{i+1}", random.randint(1, 5)) for i in range(count)]

villages = [
    create_village("Village1", random.randint(3, 5)),
    create_village("Village2", random.randint(3, 5)),
    create_village("Village3", random.randint(3, 5)),
]
gladiator = Gladiator("Maksimus", 7)

for village in villages:
    for peasant in village:
        peasant.speak()
        gladiator.recruit(peasant)

gladiator.show_legion()

gladiator.show_legion()

gladiator.train_legion()
print("\nAfter training:")
gladiator.show_legion()

        
#Абстра́ктный ме́тод (или чистый виртуальный метод (pure virtual method — часто неверно переводится как чисто виртуальный метод)) — в объектно-ориентированном программировании,
#метод класса, реализация для которого отсутствует. Класс,
#содержащий абстрактные методы, также принято называть абстрактным (там же и пример).    