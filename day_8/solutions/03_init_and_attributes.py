# ---------------------------------------------------------
# SOLUTION 3: __init__ AND ATTRIBUTES
# ---------------------------------------------------------
# __init__ runs AUTOMATICALLY when you create a new object.
# `self` refers to "this particular object" — that's how data sticks to it.


# EXERCISE 1: Book class.
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

b1 = Book("Clean Code", "Robert Martin", 431)
b2 = Book("Python Crash Course", "Eric Matthes", 544)
b3 = Book("The Pragmatic Programmer", "David Thomas", 320)

for b in (b1, b2, b3):
    print(f"'{b.title}' by {b.author} — {b.pages} pages")


# EXERCISE 2: Employee with a default salary.
class Employee:
    def __init__(self, name, department, salary=30000):
        self.name = name
        self.department = department
        self.salary = salary

emp1 = Employee("Alice", "Engineering")
emp2 = Employee("Bob", "Sales", 45000)
emp3 = Employee("Carol", "HR", 38000)

for e in (emp1, emp2, emp3):
    print(f"{e.name} ({e.department}) — Rs. {e.salary}")


# EXERCISE 3: Computed attributes — calculated once inside __init__.
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14159 * radius * radius
        self.circumference = 2 * 3.14159 * radius

for r in (5, 10, 15):
    c = Circle(r)
    print(f"radius={c.radius}, area={c.area:.2f}, circ={c.circumference:.2f}")


# EXERCISE 4: Understanding self.
class Counter:
    def __init__(self, start=0):
        self.value = start

c1 = Counter()           # start defaults to 0
c2 = Counter(10)
c3 = Counter(100)

c1.value += 5            # 0 + 5
c2.value += 5            # 10 + 5

print(c1.value)          # → 5
print(c2.value)          # → 15
print(c3.value)          # → 100   (never modified)


# EXERCISE 5: Temperature class.
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
        self.fahrenheit = (celsius * 9 / 5) + 32
        self.kelvin = celsius + 273.15

for c in (0, 100, -40):
    t = Temperature(c)
    print(f"{t.celsius}°C → {t.fahrenheit}°F, {t.kelvin}K")
