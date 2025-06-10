import random
from abc import ABC, abstractmethod

# Абстрактный класс Человек
class Person(ABC):
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    @abstractmethod
    def speak(self):
        pass

# Класс Крестьянин
class Peasant(Person):
    def __init__(self, name, strength):
        super().__init__(name, strength)
        self.ready_to_join = random.choice([True, False])

    def speak(self):
        print(f"{self.name}: Я простой крестьянин...")

# Класс Гладиатор
class Gladiator(Person):
    def __init__(self, name, strength):
        super().__init__(name, strength)
        self.legion = []

    def speak(self):
        print(f"{self.name}: За Рим!")

    def recruit(self, peasant):
        if len(self.legion) >= 10:
            print("Легион полон. Нельзя завербовать больше.")
            return
        if peasant.ready_to_join and self.strength > 5:
            print(f"{peasant.name} присоединился к легиону.")
            self.legion.append(peasant)
        else:
            print(f"{peasant.name} отказался или слишком слаб.")

    def show_legion(self):
        print("\n=== Легион Максимуса ===")
        if not self.legion:
            print("Легион пуст.")
        for member in self.legion:
            print(f"- {member.name}, сила: {member.strength}")

    def train_legion(self):
        print("\nТренировка легиона...")
        for member in self.legion:
            member.strength += 2

# Функция создания деревни
def create_village(name, count):
    villagers = []
    for i in range(count):
        villager_name = f"{name}_крестьянин{i+1}"
        strength = random.randint(1, 10)
        villagers.append(Peasant(villager_name, strength))
    hostile = random.choice([True, False])
    return {"name": name, "villagers": villagers, "hostile": hostile}

# Создание деревень
villages = [
    create_village("Гачиваново", random.randint(3, 5)),
    create_village("Стыдливые Холмы", random.randint(3, 5)),
    create_village("Азафур", random.randint(3, 5)),
    create_village("Праховка", random.randint(3, 5)),
]

# Гладиатор
gladiator = Gladiator("Максимус", 7)

# Путешествие по деревням
for village in villages:
    print(f"\n== Деревня: {village['name']} ==")
    if village["hostile"]:
        print("Деревня враждебна! Максимус уходит дальше.")
        continue
    else:
        print("Деревня мирная. Попытка вербовки...")
        for villager in village["villagers"]:
            villager.speak()
            gladiator.recruit(villager)

# Показ легиона
gladiator.show_legion()

# Тренировка
gladiator.train_legion()

# Повторный показ после тренировки
gladiator.show_legion()

        
#Абстра́ктный ме́тод (или чистый виртуальный метод (pure virtual method — часто неверно переводится как чисто виртуальный метод)) — в объектно-ориентированном программировании,
#метод класса, реализация для которого отсутствует. Класс,
#содержащий абстрактные методы, также принято называть абстрактным (там же и пример).    
