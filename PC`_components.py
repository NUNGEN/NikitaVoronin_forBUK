import random

class Component:
    def __init__(self, model, manufacturer, power_usage):
        self.model = model
        self.manufacturer = manufacturer
        self.power_usage = power_usage
        self.status = "Unknown"

    def get_info(self):
        print("Model:", self.model)
        print("Manufacturer:", self.manufacturer)
        print("Power Usage:", self.power_usage, "W")
        print("Status:", self.status)

    def run_diagnostics(self):
        pass


class CPU(Component):
    def __init__(self, model, manufacturer, power_usage, cores, frequency):
        super().__init__(model, manufacturer, power_usage)
        self.cores = cores
        self.frequency = frequency
        self.temperature = 0

    def run_diagnostics(self):
        self.temperature = random.randint(40, 100)
        if self.temperature > 85:
            print("CPU is overheating!")
            self.status = "Overheating"
            return False
        self.status = "OK"
        return True


class GPU(Component):
    def __init__(self, model, manufacturer, power_usage, vram, frequency, driver_installed):
        super().__init__(model, manufacturer, power_usage)
        self.vram = vram
        self.frequency = frequency
        self.driver_installed = driver_installed

    def run_diagnostics(self):
        if not self.driver_installed or self.vram < 2:
            self.status = "Missing drivers or low VRAM"
            return False
        self.status = "OK"
        return True


class RAM(Component):
    def __init__(self, model, manufacturer, power_usage, size, frequency, usage):
        super().__init__(model, manufacturer, power_usage)
        self.size = size
        self.frequency = frequency
        self.usage = usage

    def run_diagnostics(self):
        if (self.usage > 95 and self.usage < 100) or self.size < 2:
            self.status = "Memory error"
            return False
        self.status = "OK for now"
        return True


class Storage(Component):
    def __init__(self, model, manufacturer, power_usage, capacity, read_speed, bad_sectors, storage_type):
        super().__init__(model, manufacturer, power_usage)
        self.capacity = capacity
        self.read_speed = read_speed
        self.bad_sectors = bad_sectors
        self.storage_type = storage_type

    def run_diagnostics(self):
        if self.read_speed < 10 or self.bad_sectors > 100:
            self.status = "Storage error"
            return False
        self.status = "Memory is OK"
        return True


class Computer:
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def totalPower(self):
        total = 0
        for c in self.components:
            total += c.power_usage
        return total

    def diagnosting_all(self):
        print("Running diagnostics for whole list of components:")
        for component in self.components:
            result = component.run_diagnostics()
            print("Component:", component.model)
            print("Status:", component.status)
            print("Diagnosis Passed:", result)


cpu = CPU("i7-12700", "Intel", 125, 12, 3.8)
gpu = GPU("RTX 3080", "Nvidia", 320, 10, 1.7, True)
ram = RAM("Corsair Vengeance", "Corsair", 30, 16, 3200, 70)
storage = Storage("Samsung 970 EVO", "Samsung", 5, 1000, 3000, 0, "SSD")

my_pc = Computer()
my_pc.add_component(cpu)
my_pc.add_component(gpu)
my_pc.add_component(ram)
my_pc.add_component(storage)

my_pc.diagnosting_all()
print("Total Power Usage:", my_pc.totalPower(), "W")
