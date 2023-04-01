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


my_auto = Auto(brand="Toyota", age=5, mark="Camry", color="red", weight=1500)
my_auto.move()
my_auto.stop()
my_auto.birthday()