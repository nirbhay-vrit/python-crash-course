# ---------------------------------------------------------
# SOLUTION 1: INHERITANCE
# ---------------------------------------------------------
# Inheritance lets a child class REUSE everything from a parent class,
# then add or override what's different.


# EXERCISE 1: Vehicle → Car.
class Vehicle:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    def start_engine(self):
        print(f"{self.make} engine started.")


class Car(Vehicle):
    def __init__(self, make, year, num_doors):
        super().__init__(make, year)        # let the parent set make + year
        self.num_doors = num_doors

    def honk(self):
        print(f"{self.make} goes: Beep beep!")


car = Car("Toyota", 2024, 4)
car.start_engine()       # inherited from Vehicle
car.honk()               # added by Car
print(car.year)


# EXERCISE 2: Method overriding.
class Employee:
    def __init__(self, name, hourly_rate):
        self.name = name
        self.hourly_rate = hourly_rate

    def weekly_pay(self):
        return self.hourly_rate * 40       # default: full-time hours


class FullTimeEmployee(Employee):
    # No changes needed — inherits weekly_pay() as-is.
    pass


class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_per_week):
        super().__init__(name, hourly_rate)
        self.hours_per_week = hours_per_week

    def weekly_pay(self):
        # OVERRIDE — same method name, new behaviour.
        return self.hourly_rate * self.hours_per_week


ft = FullTimeEmployee("Alice", 20)
pt = PartTimeEmployee("Bob", 15, 25)
print(ft.weekly_pay())   # 800
print(pt.weekly_pay())   # 375


# EXERCISE 3: super() to EXTEND __init__.
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)        # reuse parent's setup...
        self.breed = breed                 # ...then add our own attribute

    def profile(self):
        print(f"{self.name} is a {self.breed}, aged {self.age}")


rex = Dog("Rex", 4, "Labrador")
rex.info()
rex.profile()


# EXERCISE 4: isinstance() and issubclass().
class LivingThing:
    pass

class Plant(LivingThing):
    pass

class Animal2(LivingThing):
    pass

class Dog2(Animal2):
    pass

fido = Dog2()

# isinstance(obj, Class) → True if obj is of Class OR any of its parents.
print(isinstance(fido, Dog2))           # True
print(isinstance(fido, Animal2))        # True  (Dog2 inherits from Animal2)
print(isinstance(fido, LivingThing))    # True  (and from LivingThing)
print(isinstance(fido, Plant))          # False (Plant is a SIBLING)

# issubclass(Child, Parent) checks the class tree (not an object).
print(issubclass(Dog2, Animal2))        # True
print(issubclass(Animal2, LivingThing)) # True
print(issubclass(Plant, Animal2))       # False


# EXERCISE 5 (CHALLENGE): School system.
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Student(Person):
    def __init__(self, name, email, student_id, grades=None):
        super().__init__(name, email)
        self.student_id = student_id
        # IMPORTANT: don't use grades=[] as a default — mutable defaults
        # are shared across calls. Use None then build a fresh list here.
        self.grades = list(grades) if grades else []

    def add_grade(self, score):
        self.grades.append(score)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def status(self):
        if self.average() >= 50:
            print(f"{self.name}: PASS (avg {self.average():.1f})")
        else:
            print(f"{self.name}: FAIL (avg {self.average():.1f})")


class Teacher(Person):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

    def introduce(self):
        print(f"I teach {self.subject}")


student = Student("Maya", "maya@school.edu", "S001")
student.add_grade(72)
student.add_grade(48)
student.add_grade(85)
print(f"Average: {student.average():.2f}")
student.status()

teacher = Teacher("Mr. Sharma", "sharma@school.edu", "Mathematics")
teacher.introduce()
