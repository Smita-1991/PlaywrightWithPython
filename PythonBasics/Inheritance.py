class Car:
    def __init__(self, window, door, engine_type):
        self.window = window
        self.door = door
        self.engine_type = engine_type

    def drive(self):
        print(f"The person will drive the {self.engine_type} car")

class Tesla(Car):
    def __init__(self,window,door,engine_type,is_selfDriving):
        super().__init__(window, door, engine_type)
        self.is_selfDriving = is_selfDriving

    def selfDriving(self):
        print(f"Tesla supports self driving: {self.is_selfDriving}")

tesla1=Tesla(4, 4, "Electric", True)
tesla1.drive()
tesla1.selfDriving()



class Animal:
    def __init__(self, name):
        self.name = name

    def speek(self):
        print(f"{self.name} makes a sound.")

class Pet():
    def __init__(self,owner_name):
        self.owner_name = owner_name

class Dog(Animal,Pet):
    def __init__(self, name, owner_name):
        Animal.__init__(self, name)
        Pet.__init__(self, owner_name)

    def speek(self):
        print(f"{self.name} barks.")


dog1 = Dog("Buddy", "John")
dog1.speek()