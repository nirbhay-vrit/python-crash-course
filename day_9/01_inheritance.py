# ---------------------------------------------------------
# DAY 9 | TOPIC 1: INHERITANCE — Reusing and Extending Classes
# One class can inherit attributes and methods from another.
# Write shared code ONCE in a parent — all children get it free.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: THE PROBLEM INHERITANCE SOLVES
# ─────────────────────────────────────────────────────────
# Imagine tracking Dogs and Cats. Both have name + age.
# Both can eat() and sleep(). Without inheritance you duplicate:

class DogNoInheritance:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def eat(self):              # DUPLICATED in Cat below!
        print(f"{self.name} is eating.")

    def sleep(self):            # DUPLICATED in Cat below!
        print(f"{self.name} is sleeping.")

    def bark(self):
        print(f"{self.name} says: Woof!")


class CatNoInheritance:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def eat(self):              # EXACT COPY from Dog — bad!
        print(f"{self.name} is eating.")

    def sleep(self):            # EXACT COPY from Dog — bad!
        print(f"{self.name} is sleeping.")

    def meow(self):
        print(f"{self.name} says: Meow!")

# eat() and sleep() are identical → DRY (Don't Repeat Yourself) violation.
# Fix: put shared code in a PARENT class, inherit it in the children.


# ─────────────────────────────────────────────────────────
# SECTION 2: BASIC INHERITANCE SYNTAX
# ─────────────────────────────────────────────────────────
# Syntax: class Child(Parent):
# The child gets ALL attributes and methods from the parent automatically.

class Animal:                   # PARENT / BASE class
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def describe(self):
        print(f"{self.name} is {self.age} years old.")


class Dog(Animal):              # CHILD class — inherits from Animal
    def bark(self):             # adds its own unique method
        print(f"{self.name} says: Woof!")


class Cat(Animal):              # CHILD class — inherits from Animal
    def meow(self):             # adds its own unique method
        print(f"{self.name} says: Meow!")


print("--- Basic inheritance ---")
rex  = Dog("Rex", 3)
luna = Cat("Luna", 2)

rex.eat()         # inherited from Animal → Rex is eating.
rex.sleep()       # inherited from Animal → Rex is sleeping.
rex.bark()        # Dog's own method      → Rex says: Woof!
rex.describe()    # inherited             → Rex is 3 years old.

luna.eat()        # inherited from Animal → Luna is eating.
luna.meow()       # Cat's own method      → Luna says: Meow!

# Key terms:
#   Animal = parent / base / super class
#   Dog    = child / derived / sub class
#   Dog inherits Animal → "Dog IS-A Animal"


# ─────────────────────────────────────────────────────────
# SECTION 3: super() — EXTENDING __init__
# ─────────────────────────────────────────────────────────
# When the child needs its OWN extra attributes in addition
# to the parent's, use super().__init__() to call the parent
# constructor first, then add child-specific attributes.

class Animal2:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def describe(self):
        print(f"{self.name} ({self.age} yrs)")


class Dog2(Animal2):
    def __init__(self, name, age, breed):   # ← adds 'breed'
        super().__init__(name, age)         # runs Animal2.__init__ first
        self.breed = breed                  # then adds its own attribute

    def introduce(self):
        print(f"I am {self.name}, a {self.breed}, {self.age} years old.")


class Cat2(Animal2):
    def __init__(self, name, age, indoor):  # ← adds 'indoor'
        super().__init__(name, age)
        self.indoor = indoor

    def status(self):
        loc = "indoor" if self.indoor else "outdoor"
        print(f"{self.name} is an {loc} cat.")


print("\n--- super() ---")
rex2  = Dog2("Rex",  3, "Labrador")
luna2 = Cat2("Luna", 2, True)

rex2.describe()     # from Animal2 → Rex (3 yrs)
rex2.introduce()    # I am Rex, a Labrador, 3 years old.
luna2.describe()    # from Animal2 → Luna (2 yrs)
luna2.status()      # Luna is an indoor cat.


# ─────────────────────────────────────────────────────────
# SECTION 4: METHOD OVERRIDING
# ─────────────────────────────────────────────────────────
# A child class can OVERRIDE a parent method by defining
# a method with the SAME name. Python always runs the
# most specific (child) version — called Method Resolution Order.

class Animal3:
    def __init__(self, name):
        self.name = name

    def speak(self):                        # parent version
        print(f"{self.name} makes a sound.")


class Dog3(Animal3):
    def speak(self):                        # overrides parent
        print(f"{self.name} says: Woof!")


class Cat3(Animal3):
    def speak(self):                        # overrides parent
        print(f"{self.name} says: Meow!")


class Fish3(Animal3):
    pass                                    # no override → uses parent's speak()


print("\n--- Method overriding ---")
animals = [Dog3("Rex"), Cat3("Luna"), Fish3("Nemo")]
for a in animals:
    a.speak()
# Rex says: Woof!
# Luna says: Meow!
# Nemo makes a sound.   ← no override, falls back to parent


# ─────────────────────────────────────────────────────────
# SECTION 5: isinstance() AND issubclass()
# ─────────────────────────────────────────────────────────
# isinstance(obj, Class) → True if obj is an instance of Class
#   OR any subclass of it. Useful for type-checking.
# issubclass(A, B) → True if A inherits from B.

class Vehicle:
    pass

class Car(Vehicle):
    pass

class ElectricCar(Car):         # multi-level: ElectricCar → Car → Vehicle
    pass

my_car = ElectricCar()

print("\n--- isinstance / issubclass ---")
print(isinstance(my_car, ElectricCar))   # True  — direct class
print(isinstance(my_car, Car))           # True  — parent
print(isinstance(my_car, Vehicle))       # True  — grandparent
print(isinstance(my_car, str))           # False — unrelated type

print(issubclass(ElectricCar, Car))      # True
print(issubclass(ElectricCar, Vehicle))  # True
print(issubclass(Car, ElectricCar))      # False — reversed!

# isinstance is safer than type() for inheritance:
print("\n--- isinstance vs type ---")
print(type(my_car) == Car)              # False — type() is EXACT match only
print(isinstance(my_car, Car))          # True  — isinstance checks hierarchy
