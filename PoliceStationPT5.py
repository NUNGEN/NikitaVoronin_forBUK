#class PoliceStation:
    
class PoliceOfficer:
    def __init__(self,name,badge_number,cases):
        self.name = ["Peter Pot","Alexander Makovski","Seraphim Bogomdanov"] #имя
        self.badge_number = badge_number#номер удостоверения
        self.cases = cases(Case) #список дел (объекты Case)
        
    def assign_case(Case): #– прикрепляет дело к полицейскому
        if name(self) + Case() == True:
            print("Mission signed by: "("name"))
        else:
            print("Name is not defined")
        
    def get_case_by_id(case_id): # – находит конкретное дело по ID
        find("Idlist",1)
        
    def get_summary(): #– возвращает сводку (например, сколько дел открыто и закрыто)
        
        return
    def get_info(): # – возвращает имя полицейского и номер удостоверения
        name(self)
        print()
        return
        
        
class Case:
    def __init__(self,cases,case_id,description,status,events):
        self.case_id = case_id(self,IdList)
    def Idlist('cases'):
    ['Case№1', 'Case№2', 'Case№3']#– уникальный идентификатор дела
        self.description = description
       #({f}"Case №1 : ) #– описание дела #,"Case №2","Case №3
        #print("Case №1%(Case№1)s. Мне %(age)d лет." % {"Case №1": name, "age": age})
        print description(f"Middle aged man, known as Fjodor Rusanov stole a homemade bread in amount of 5 kilograms from a local Tallinn bakery: {self.Case№1}")
        self.status = StatusIs()#– статус: "open" или "closed"
    def StatusIs(self,status):
        
        if status == status_open(True)
            print("Current status is :"("status_open"))
        else:
            status == status_closed(True)
            print("Current status is :"("status_closed"))
            
            return
        self.status_open = status_open
        self.status_closed = status_closed
        self.events = events(Event) #– список событий (объекты Event)
        
    def add_event(event): #– добавляет событие в историю
    
    def close_case(): #– закрывает дело
    
    def get_timeline(): # – возвращает список событий в хронологическом порядке
    
    def __get_status():
    #get_description(), get_case_id()
    
    
class Event:
    def __init__(self,cases,case_id,description,status,events):
        
    self.timestamp = timestamp#– автоматически устанавливаемая дата и время
    
    self.note = note# – описание события
    
    self.officer_name = #– имя полицейского, добавившего событие



    def __str__(): #– возвращает строку с информацией о событии в красивом формате