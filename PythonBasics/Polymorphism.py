class Animal:
    def speek(self):
        print("Animal makes a sound.")

##Derived class 1
class Dog(Animal):
    def speek(self):
        print("Dog barks.")

##Derived class 2
class Cat(Animal):
    def speek(self):
        print("Cat meows.")

def animal_speek(animal):
   animal.speek()

dog=Dog()
cat=Cat()

dog.speek()

animal_speek(dog)

cat.speek()


class Shape:
    def area(self):
        return "The area of the shape is calculated."

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        return 0.5 * self.base * self.height

def print_area(shape):
    print(f"The area of the shape is: {shape.area()}")

rectangle=Rectangle(4,5)
triangle=Triangle(4,5)

print_area(rectangle)
print_area(triangle)

