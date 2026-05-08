# ---------------------------------------------------------
# DAY 9 | TOPIC 4: SPECIAL METHODS — Making Objects Feel Native
# Special (dunder) methods let your objects work with
# Python's built-in functions: print(), len(), +, ==, etc.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: WHAT ARE SPECIAL METHODS?
# ─────────────────────────────────────────────────────────
# Python uses "dunder" (double underscore) methods internally.
# When you call print(obj)  → Python calls obj.__str__()
# When you call len(obj)    → Python calls obj.__len__()
# When you write a == b     → Python calls a.__eq__(b)
# When you write a + b      → Python calls a.__add__(b)
#
# By defining these in your class, your objects behave
# just like built-in types — natural and Pythonic.

# Without __str__:
class PointNoStr:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = PointNoStr(3, 4)
print(p)   # <__main__.PointNoStr object at 0x...> — not helpful!


# ─────────────────────────────────────────────────────────
# SECTION 2: __str__ AND __repr__
# ─────────────────────────────────────────────────────────
# __str__  → called by print() and str()
#            Should be human-readable.
# __repr__ → called by repr() and in the REPL / debugger
#            Should be unambiguous, ideally show how to recreate the object.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):                  # for humans
        return f"Point({self.x}, {self.y})"

    def __repr__(self):                 # for developers / debugging
        return f"Point(x={self.x}, y={self.y})"


print("\n--- __str__ and __repr__ ---")
p1 = Point(3, 4)
print(p1)           # uses __str__  → Point(3, 4)
print(str(p1))      # uses __str__  → Point(3, 4)
print(repr(p1))     # uses __repr__ → Point(x=3, y=4)


class Book:
    def __init__(self, title, author, pages):
        self.title  = title
        self.author = author
        self.pages  = pages

    def __str__(self):
        return f'"{self.title}" by {self.author} ({self.pages} pages)'

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.pages})"


b = Book("1984", "George Orwell", 328)
print(b)        # "1984" by George Orwell (328 pages)
print(repr(b))  # Book('1984', 'George Orwell', 328)


# ─────────────────────────────────────────────────────────
# SECTION 3: __len__ AND __contains__
# ─────────────────────────────────────────────────────────
# __len__      → called by len()
# __contains__ → called by the `in` operator

class Library:
    def __init__(self, name):
        self.name  = name
        self.books = []

    def add(self, book_title):
        self.books.append(book_title)

    def __len__(self):                      # enables len(library)
        return len(self.books)

    def __contains__(self, title):          # enables "title" in library
        return title in self.books

    def __str__(self):
        return f"{self.name} Library ({len(self)} books)"


print("\n--- __len__ and __contains__ ---")
lib = Library("City")
lib.add("1984")
lib.add("Dune")
lib.add("Brave New World")

print(lib)                      # City Library (3 books)
print(len(lib))                 # 3
print("Dune" in lib)            # True
print("Harry Potter" in lib)    # False


# ─────────────────────────────────────────────────────────
# SECTION 4: __eq__ AND __lt__ — COMPARISON OPERATORS
# ─────────────────────────────────────────────────────────
# __eq__ → == operator
# __lt__ → <  operator (also enables sorted() if defined)

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa  = gpa

    def __str__(self):
        return f"{self.name} (GPA: {self.gpa})"

    def __eq__(self, other):            # enables s1 == s2
        return self.gpa == other.gpa

    def __lt__(self, other):            # enables s1 < s2 and sorted()
        return self.gpa < other.gpa


print("\n--- __eq__ and __lt__ ---")
alice = Student("Alice", 3.8)
bob   = Student("Bob",   3.5)
carol = Student("Carol", 3.8)

print(alice == carol)           # True  — same GPA
print(alice == bob)             # False — different GPA
print(bob < alice)              # True  — Bob's GPA is lower

students = [alice, bob, carol]
ranked = sorted(students)       # sorted() uses __lt__
for s in ranked:
    print(" ", s)
# Bob   (GPA: 3.5)
# Alice (GPA: 3.8)
# Carol (GPA: 3.8)


# ─────────────────────────────────────────────────────────
# SECTION 5: __add__ — OPERATOR OVERLOADING
# ─────────────────────────────────────────────────────────
# You can make + work between your own objects.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):           # enables v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


print("\n--- __add__ (operator overloading) ---")
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2        # Python calls v1.__add__(v2)

print(v1)           # Vector(1, 2)
print(v2)           # Vector(3, 4)
print(v3)           # Vector(4, 6)
print(f"Magnitude of v3: {v3.magnitude():.2f}")  # 7.21


# ─────────────────────────────────────────────────────────
# QUICK REFERENCE — COMMON DUNDER METHODS
# ─────────────────────────────────────────────────────────
# __init__     → called on creation:      obj = MyClass()
# __str__      → str / print:             print(obj)
# __repr__     → repr / debugger:         repr(obj)
# __len__      → length:                  len(obj)
# __contains__ → membership test:         x in obj
# __eq__       → equality:               obj1 == obj2
# __lt__       → less-than / sorting:     obj1 < obj2
# __add__      → addition:               obj1 + obj2
# __getitem__  → indexing:               obj[0]
# __iter__     → iteration:              for x in obj:
