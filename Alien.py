from rich.console import Console
from rich.table import Table
from time import sleep
from random import random

console = Console()
for i in range(5, 0, -1):
    console.log(f"An allien will attack your spaceship after {i} minutes")
    sleep(1)
console.log("You are alreadty attacked")

class CrewMember:
    def __init__(self,name,role):
        self.name = name
        self.role = role
        self.hp = 100
        self.strenght = random.randint(15,30)
        self.status = True
    #name, role, hp, strenght(random), status    ,hp,strenght,status
class Alien:
    def __init__(self):
        self.aggresion = random.randint(1,10)
        self.hp = 134
        
    def attack():
        pass
    
    def injure():
        pass
    #aggresion, hp
class Ship:
    def __init__(self,status,rooms):
        self.status = True
        self.rooms = []
        
    def trigger_alarm():
    #status, rooms
        
class Misiion:
    def __init__(self,crewlist):
        self.crew = crewlist
        self.alien = Alien()
        self.ship = Ship()
    #crew, alien, ship
    def summary(self):
        table = Table(Title="Crew members")
        table.add_column("Nimi", style="yellow")
        table.add_column("Nimi", style="green")
        table.add_column("Nimi", style="red")
        table.add_column("Nimi", style="purple")
        
        for crewMember in self.crew:
            if crewMember.status == False:
                status = "Died"
            else:
                status = "Alive"
                
            table.add_row(crewMember.name,crewMember.role,str(crewMember.hp),status)
        console.print(table)
        
crew = [CrewMember("Ripli","Captain"),
    CrewMember("Dallas","Sailor"),
    CrewMember("Esh","Science officer"),
    CrewMember("Parker","Engineer")
]

mission1 = Mission(crew)
mission1.summary()
            