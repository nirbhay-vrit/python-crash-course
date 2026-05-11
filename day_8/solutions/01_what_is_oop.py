# ---------------------------------------------------------
# SOLUTION 1: WHAT IS OOP?
# ---------------------------------------------------------


# EXERCISE 1: Add a third book using the same pattern.
# Notice how messy this is — that's the WHOLE point. OOP solves it!
book1_title  = "Python Crash Course"
book1_author = "Eric Matthes"
book1_pages  = 544

book2_title  = "Clean Code"
book2_author = "Robert Martin"
book2_pages  = 431

book3_title  = "The Pragmatic Programmer"
book3_author = "David Thomas"
book3_pages  = 320

print(f"Title: {book1_title}, Author: {book1_author}, Pages: {book1_pages}")
print(f"Title: {book2_title}, Author: {book2_author}, Pages: {book2_pages}")
print(f"Title: {book3_title}, Author: {book3_author}, Pages: {book3_pages}")


# EXERCISE 2: Match the vocabulary.
class Car:
    def __init__(self, brand, colour):
        self.brand  = brand
        self.colour = colour

    def honk(self):
        print(f"{self.brand} goes: Beep!")

my_car = Car("Toyota", "red")
my_car.honk()

print("Car is a      : class")        # Car is a class (a blueprint)
print("my_car is an  : object")       # my_car is an object (an instance of Car)
print("my_car.brand  : attribute")    # data stored on the object
print("my_car.honk() : method")       # a function that belongs to the object


# EXERCISE 3: Pizza class skeleton.
# Attributes a Pizza might have:
# 1. size (small / medium / large)
# 2. toppings (a list)
# 3. crust_type (thin / thick / stuffed)

# Methods a Pizza might have:
# 1. add_topping(topping)
# 2. bake()

class Pizza:
    pass


# EXERCISE 4: True or False.
# a) A class is a blueprint, objects are built from it.           → True
# b) You can only create ONE object from a class.                 → False (many)
# c) Attributes store data; methods define behaviour.             → True
# d) OOP helps keep related data bundled together.                → True
# e) You must write a new class every time you need a new object. → False (re-use!)
