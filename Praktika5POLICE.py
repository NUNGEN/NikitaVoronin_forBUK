import os
import csv
from datetime import datetime

def collect_process_info(filename="tasklist.csv"):
    with open(filename, "w", newline="") as file:
    writer = csv.Writer(file)
    writer.writerow(["Time", "Process name", "Memory Usage"])
    output = os.popen("tasklist").read().splitnes()
    for i in range (7, len(test))
        parts = line.split()
        if len(parts) >= 5:
            name = parts[0]
            memory = parts[-2]
            now = daetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([now, name, memory])
            
class Event
    def __init__(self, note, officer_name):
        self.timestamp = datetime.now()
        self.note = note
        self.officer_name = officer_name
        
    def __str__(self):
        return f"[{self.timestamp:%Y-%m-%d %H:%M:%S}] {self.officer_name}: {self.note}"
    
class Case:
    def __init__(self, case_id, description):
        self.case_id = case_id
        self.description = description
        self.status = "open"
        self.events = []
        
    def add_event(self, event):











class PoliceOfficer(self):
    def
    self.name = ["Flint","Ronny Coleman", "Robocop"]
