import time

class Auto:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1
        
class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load
        
    def move(self):
        print("attention")
        super().move()
        
    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)
        
class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed
        
    def move(self):
        super().move()
        print("max speed is", self.max_speed)


# створення обʼєктів 
truck1 = Truck(brand="Volvo", age=2, mark="FH16", max_load=20000)
truck2 = Truck(brand="Mercedes", age=3, mark="Actros", max_load=18000)
car1 = Car(brand="Toyota", age=5, mark="Camry", max_speed=180)
car2 = Car(brand="Nissan", age=4, mark="GT-R", max_speed=250)

truck1.move()
truck1.load()
truck2.move()
truck2.load()
car1.move()
car2.move()
truck1.stop()
truck2.birthday()
car1.stop()
car2.birthday()

print(car2.age)
print(truck1.brand)
print(car2.mark)