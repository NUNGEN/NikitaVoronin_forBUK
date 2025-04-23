import random
from abc import ABC, abstractmethod

# 1. Абстрактный класс Человек
class Person(ABC):
    def init(self, name, strength):
        self.name = name
        self.strength = strength

    @abstractmethod
    def speak(self):
        pass

# 2. Класс Крестьянин
class Peasant(Person):
    def init(self, name, strength):
        super().init(name, strength)
        self.ready_to_join = random.choice([True, False])

    def speak(self):
        print(f"{self.name}: *молчит по-крестьянски*")

# 3. Класс Гладиатор
class Gladiator(Person):
    def init(self, name, strength):
        super().init(name, strength)
        self.legion = []

    def speak(self):
        print(f"{self.name}: *боевой клич*")

    def recruit(self, peasant):
        if len(self.legion) >= 10:
            return
        if peasant.ready_to_join and self.strength > 5:
            self.legion.append(peasant)

    def show_legion(self):
        print("Легион:")
        for p in self.legion:
            print(f"- {p.name}, сила: {p.strength}")

    def train_legion(self):
        for p in self.legion:
            p.strength += 2

# 4. Создание деревень
def create_village(name_prefix, count):
    return [Peasant(f"{name_prefix}_{i+1}", random.randint(1, 5)) for i in range(count)]

villages = [
    create_village("деревня1", random.randint(3, 5)),
    create_village("деревня2", random.randint(3, 5)),
    create_village("деревня3", random.randint(3, 5)),
]

# 5. Гладиатор идет по деревням
gladiator = Gladiator("Максимус", 7)

for village in villages:
    for peasant in village:
        peasant.speak()
        gladiator.recruit(peasant)

gladiator.show_legion()

# Тренировка
gladiator.train_legion()
print("\nПосле тренировки:")
gladiator.show_legion()