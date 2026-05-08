# ---------------------------------------------------------
# DAY 9 | TOPIC 2: POLYMORPHISM — One Interface, Many Behaviours
# Poly = many, morph = forms.
# Same method name, different behaviour depending on the object.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: WHAT IS POLYMORPHISM?
# ─────────────────────────────────────────────────────────
# Polymorphism means different classes can share the same
# method NAME but each class defines its OWN behaviour for it.
#
# Real-world analogy:
#   "speak" means different things to a dog, cat, and human.
#   The interface (speak) is the same — the result is different.

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says: Woof!"


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says: Meow!"


class Bird:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says: Tweet!"


print("--- Same interface, different behaviour ---")
animals = [Dog("Rex"), Cat("Luna"), Bird("Tweety")]

for animal in animals:
    print(animal.speak())   # same call — different output each time!

# Rex says: Woof!
# Luna says: Meow!
# Tweety says: Tweet!
#
# We call .speak() on every object the same way.
# We don't need to know what TYPE the object is.
# That is the power of polymorphism.


# ─────────────────────────────────────────────────────────
# SECTION 2: POLYMORPHISM WITH INHERITANCE
# ─────────────────────────────────────────────────────────
# The most common pattern: a parent defines a method,
# each child OVERRIDES it with its own version.

class Shape:
    def __init__(self, colour):
        self.colour = colour

    def area(self):               # parent version — meant to be overridden
        return 0

    def describe(self):           # shared — uses self.area() polymorphically
        print(f"{self.colour} {self.__class__.__name__}: area = {self.area():.2f}")


class Circle(Shape):
    def __init__(self, colour, radius):
        super().__init__(colour)
        self.radius = radius

    def area(self):               # overrides Shape.area()
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, colour, width, height):
        super().__init__(colour)
        self.width  = width
        self.height = height

    def area(self):               # overrides Shape.area()
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, colour, base, height):
        super().__init__(colour)
        self.base   = base
        self.height = height

    def area(self):               # overrides Shape.area()
        return 0.5 * self.base * self.height


print("\n--- Polymorphism with inheritance ---")
shapes = [
    Circle("red",    5),
    Rectangle("blue", 4, 6),
    Triangle("green", 3, 8),
]

for shape in shapes:
    shape.describe()   # describe() calls self.area() — which version?
                       # whichever version belongs to THAT object!

# red Circle:    area = 78.54
# blue Rectangle: area = 24.00
# green Triangle: area = 12.00


# ─────────────────────────────────────────────────────────
# SECTION 3: DUCK TYPING — Python's Natural Polymorphism
# ─────────────────────────────────────────────────────────
# "If it walks like a duck and quacks like a duck, it's a duck."
#
# In Python, you don't NEED inheritance for polymorphism.
# If an object has the right method, Python will call it —
# regardless of what class it belongs to.

class Printer:
    def render(self):
        print("Printing document...")

class Screen:
    def render(self):
        print("Displaying on screen...")

class PDFExporter:
    def render(self):
        print("Exporting to PDF...")

# None of these share a parent class, but they all have render()!
def show_output(device):      # works with ANY object that has .render()
    device.render()


print("\n--- Duck typing ---")
devices = [Printer(), Screen(), PDFExporter()]
for device in devices:
    show_output(device)       # Python doesn't care about the class name

# Printing document...
# Displaying on screen...
# Exporting to PDF...


# ─────────────────────────────────────────────────────────
# SECTION 4: POLYMORPHISM WITH FUNCTIONS
# ─────────────────────────────────────────────────────────
# A function that accepts different object types and calls
# the same method on each — working because of polymorphism.

class Employee:
    def __init__(self, name, base_salary):
        self.name        = name
        self.base_salary = base_salary

    def calculate_pay(self):
        return self.base_salary


class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_pay(self):            # overrides: salary + bonus
        return self.base_salary + self.bonus


class Contractor(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, hourly_rate)
        self.hours_worked = hours_worked

    def calculate_pay(self):            # overrides: rate × hours
        return self.base_salary * self.hours_worked


def print_payslip(employee):            # works for any Employee type
    pay = employee.calculate_pay()
    print(f"  {employee.name}: ${pay:,.2f}")


print("\n--- Polymorphism with functions ---")
staff = [
    Employee("Alice",   5000),
    Manager("Bob",      5000, 2000),
    Contractor("Carol", 80,   160),
]

print("Payroll:")
for person in staff:
    print_payslip(person)   # same function call — different calculation each time

# Alice:  $5,000.00
# Bob:    $7,000.00
# Carol:  $12,800.00


# ─────────────────────────────────────────────────────────
# SECTION 5: __str__ — POLYMORPHISM BUILT INTO PYTHON
# ─────────────────────────────────────────────────────────
# Python itself uses polymorphism constantly.
# print() calls __str__() on the object — each class defines its own.
# len() calls __len__(). + calls __add__(). etc.

class Book:
    def __init__(self, title, author):
        self.title  = title
        self.author = author

    def __str__(self):              # what print() calls
        return f'"{self.title}" by {self.author}'


class Movie:
    def __init__(self, title, director):
        self.title    = title
        self.director = director

    def __str__(self):              # what print() calls — different output
        return f'[Movie] {self.title} — directed by {self.director}'


print("\n--- __str__ polymorphism ---")
items = [
    Book("1984", "George Orwell"),
    Movie("Inception", "Christopher Nolan"),
    Book("Dune", "Frank Herbert"),
]

for item in items:
    print(item)   # Python calls item.__str__() — each class defines its own version!
