import random
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    @abstractmethod
    def speak(self):
        pass

class Peasant(Person):
    def __init__(self, name, strength):
        super().__init__(name, strength)
        self.ready_to_join = random.choice([True, False])

    def speak(self):
        print(f"{self.name}: I'm just a humble peasant")

class Gladiator(Person):
    def __init__(self, name, strength):
        super().__init__(name, strength)
        self.legion = []

    def speak(self):
        print(f"{self.name}: For the Legion!")

    def recruit(self, peasant):
        if len(self.legion) >= 8:
            print("The legion is full. Trying to replace a weaker member")
            self.replace_weaker(peasant)
            return
        if peasant.ready_to_join and self.strength > 5 and peasant.strength > 5:
            print(f"{peasant.name} has joined the legion.")
            self.legion.append(peasant)
        else:
            print(f"{peasant.name} refused or is too weak.")

    def replace_weaker(self, new_peasant):
        for member in self.legion:
            if new_peasant.strength > member.strength:
                print(f"Replacing {member.name} with {new_peasant.name}.")
                self.legion.remove(member)
                self.legion.append(new_peasant)
                return
        print(f"{new_peasant.name} is not stronger than anyone in the legion.")

    def show_legion(self):
        print("\nLegion")
        if not self.legion:
            print("The legion is empty.")
        for member in self.legion:
            print(f"- {member.name}, strength: {member.strength}")

    def train_legion(self):
        print("\nTraining the legion...")
        for member in self.legion:
            member.strength += 2

def create_village(name, count):
    villagers = []
    for i in range(count):
        villager_name = f"{name}_peasant{i+1}"
        strength = random.randint(1, 10)
        villagers.append(Peasant(villager_name, strength))
    hostile = random.choice([True, False])
    return {"name": name, "villagers": villagers, "hostile": hostile}

villages = [
    create_village("Gachivanovo", random.randint(5, 10)),
    create_village("Shy Hills", random.randint(5, 10)),
    create_village("Azafur", random.randint(5, 10)),
    create_village("Ashiel", random.randint(5, 10)),
    create_village("Neverland", random.randint(5, 10)),
    create_village("Tunguska", random.randint(5, 10)),
    create_village("Serodile", random.randint(5, 10)),
]

gladiator = Gladiator("Maximus", 7)

for village in villages:
    print(f"\nVillage: {village['name']}")
    if village["hostile"]:
        print("The village is hostile! Maximus moves on.")
        continue
    else:
        print("The village is peaceful. Attempting recruitment.")
        for villager in village["villagers"]:
            villager.speak()
            gladiator.recruit(villager)

gladiator.show_legion()
gladiator.train_legion()
gladiator.show_legion()
        
#Абстра́ктный ме́тод (или чистый виртуальный метод (pure virtual method — часто неверно переводится как чисто виртуальный метод)) — в объектно-ориентированном программировании,
#метод класса, реализация для которого отсутствует. Класс,
#содержащий абстрактные методы, также принято называть абстрактным (там же и пример).    
