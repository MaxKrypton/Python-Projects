class vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    def seating_capacity(self, capacity):
        print(f"This is car's name is {self.name} and it has a capacity of {capacity}")
        

class bus(vehicle):
    def __init__(self, name, max_speed, height, version):
        super().__init__(name, max_speed, height, version )

    def description(self):
        print(f"This is a {self.name} which runs at a speed of {self.max_speed}")

class moto_bike(vehicle):
    def __init__(self, name, max_speed, height, version, mark):
        self.mark = mark
        super().__init__(name, max_speed, height, version)
    
    def more_description(self):
        print(f"This is a {self.name} of a height of {self.height} and it is a {self.version} and marked as {self.mark}")
        
trip_vehicle = bus("Prado", 12000, "2.3M", "2.342GX")
trip_vehicle.description()

Yamaha_motobike = moto_bike("YAMAHA", 3495, "0.6m", "Hilux-250", 5674)
Yamaha_motobike.more_description()