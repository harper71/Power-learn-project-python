class Vehicles:
    def __init__(self):
        pass
    def move(self):
        return "Moves"    
class Car(Vehicles):
    def __init__(self):
        super().__init__()
        
    def move(self):
        print("Driving 🚗")
class Plane(Vehicles):
    def __init__(self):
        super().__init__()
        
    def move(self):
        print("Flying ✈️")


car = Car()
car.move()
plane = Plane()
plane.move()