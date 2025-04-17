# class Animal:
#     def make_sound(self):
#         pass
#     
# class Dog(Animal):
#     pass
# 
# 
# dog1 = Dog()
# dog1.make_sound()
# 
# from abc import ABC,abstractmethod
# 
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
#     
# class Dog(Animal):
#     pass
# 
# dog2 = Dog()
# dog2.make_sound()

from abc import ABC, abstractmethod
import random

class Character(ABC):
    def __init__(self):
        self.state = {
            "health": 101,
            "inventory": [],
            "morale": 1.0
        }
    
    @abstractmethod
    def decide_action(self, context):
        pass
    
    @abstractmethod
    def update_action(self, cont# class Animal:
#     def make_sound(self):
#         pass
#     
# class Dog(Animal):
#     pass
# 
# 
# dog1 = Dog()
# dog1.make_sound()
# 
# from abc import ABC,abstractmethod
# 
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
#     
# class Dog(Animal):
#     pass
# 
# dog2 = Dog()
# dog2.make_sound()

from abc import ABC, abstractmethod
import random

class Character(ABC):
    def __init__(self):
        self.state = {
            "health": 101,
            "inventory": [],
            "morale": 1.0ext):
        pass

    def __str__(self):
        return f"Health: {self.state['health']}, Morale: {self.state['morale']}, Inventory: {self.state['inventory']}"

class Civilian(Character):
    def decide_action(self, context):
        if context["menace_level"] > 0.6:
            print("Civilian is hiding.")
        else:
            print("Civilian dared to combat.")
    
    def update_action(self, context):
        if context["menace_level"] > 0.6:
            self.state["morale"] -= 0.3
        else:
            self.state["morale"] += 0.05

class Criminal(Character):
    def decide_action(self, context):
        if 0.9 < context["menace_level"] < 1.1:
            print("Criminal decides to steal.")
        elif context["menace_level"] >= 1.1:
            print("Criminal decides to attack.")
        else:
            print("Criminal decides to run.")
        
    def update_action(self, context):
        if context["menace_level"] > 0.9:
            self.state["morale"] -= 0.5
        else:
            self.state["morale"] += 0.10

class Survivor(Character):
    def decide_action(self, context):
        if 0.9 < context["menace_level"] < 1.1:
            print("Survivor decides to steal.")
        elif context["menace_level"] >= 1.1:
            print("Survivor decides to attack.")
        else:
            print("Survivor decides to survive.")
        
    def update_action(self, context):
        if context["menace_level"] > 0.9:
            self.state["morale"] -= 0.5
        else:
            self.state["morale"] += 0.10

# Creating instances of the characters
civilian1 = Civilian()
criminal1 = Criminal()
survivor1 = Survivor()

# Context with detailed menace levels and character states
context = {
    "Civilian": {
        "menace_level": 0.7,
        "has_weapon": False,
        "health": 55
    },
    "Criminal": {
        "menace_level": 0.8,
        "has_weapon": True,
        "health": 85
    },
    "Survivor": {
        "menace_level": 1.2,
        "has_weapon": False,
        "health": 70
    }
}

# Randomly selecting a character from the context
random_char_name = random.choice(list(context.keys()))
random_char_data = context[random_char_name]

# Printing the selected character and event
print(f"Selected Character: {random_char_name}")
print(f"Menace Level: {random_char_data['menace_level']}")
print(f"Character Health: {random_char_data['health']}")

# Decide action based on character's menace level
if random_char_name == "Civilian":
    civilian1.decide_action(random_char_data)
    civilian1.update_action(random_char_data)
elif random_char_name == "Criminal":
    criminal1.decide_action(random_char_data)
    criminal1.update_action(random_char_data)
elif random_char_name == "Survivor":
    survivor1.decide_action(random_char_data)
    survivor1.update_action(random_char_data)

# Output updated character information
print(f"Updated State: {civilian1 if random_char_name == 'Civilian' else criminal1 if random_char_name == 'Criminal' else survivor1}")