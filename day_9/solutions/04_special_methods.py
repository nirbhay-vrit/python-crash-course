# ---------------------------------------------------------
# SOLUTION 4: SPECIAL (DUNDER) METHODS
# ---------------------------------------------------------
# "Dunder" = Double UNDERscore — e.g. __str__, __len__.
# These hook into Python's built-in operators and functions:
#   print(obj)        →  __str__
#   len(obj)          →  __len__
#   x in obj          →  __contains__
#   obj1 == obj2      →  __eq__
#   obj1 + obj2       →  __add__
#   obj1 < obj2       →  __lt__   (used by sorted())


# EXERCISE 1: __str__ controls what print() shows.
class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

    def __str__(self):
        return f'"{self.title}" ({self.year}) — {self.genre}'


m = Movie("The Matrix", 1999, "Sci-Fi")
print(m)


# EXERCISE 2: __len__ and __contains__.
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self):
        return f"Playlist '{self.name}' — {len(self)} songs"

    def __len__(self):
        return len(self.songs)

    def __contains__(self, song):
        return song in self.songs


pl = Playlist("My Favourites")
pl.add_song("Bohemian Rhapsody")
pl.add_song("Hotel California")
pl.add_song("Stairway to Heaven")

print(pl)
print(len(pl))                       # 3
print("Hotel California" in pl)      # True
print("Shape of You" in pl)          # False


# EXERCISE 3: __eq__ — define what "equal" means for your class.
class Product:
    def __init__(self, name, sku, price):
        self.name = name
        self.sku = sku
        self.price = price

    def __str__(self):
        return f"{self.name} (SKU: {self.sku}, ${self.price:.2f})"

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented        # comparing to non-Product → not equal
        return self.sku == other.sku


p1 = Product("Widget A", "SKU-001", 9.99)
p2 = Product("Widget A Deluxe", "SKU-001", 14.99)
p3 = Product("Gadget B", "SKU-002", 19.99)
print(p1 == p2)        # True  — same SKU
print(p1 == p3)        # False — different SKU


# EXERCISE 4: __add__ — overload the + operator.
class ShoppingCart:
    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __str__(self):
        return f"{self.owner}'s cart: {self.items}"

    def __add__(self, other):
        merged = ShoppingCart("merged")
        merged.items = self.items + other.items
        return merged


cart1 = ShoppingCart("Alice")
cart1.add("Book")
cart1.add("Pen")

cart2 = ShoppingCart("Bob")
cart2.add("Notebook")
cart2.add("Ruler")

merged = cart1 + cart2
print(merged)


# EXERCISE 5 (CHALLENGE): Full Temperature class.
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __str__(self):
        return f"{self.celsius}°C"

    def __repr__(self):
        # __repr__ is what you see in lists, debuggers, etc.
        return f"Temperature({self.celsius})"

    def __eq__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius == other.celsius

    def __lt__(self, other):
        # Needed by sorted() to compare two Temperatures.
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius < other.celsius

    def __add__(self, other):
        return Temperature(self.celsius + other.celsius)

    def to_fahrenheit(self):
        return (self.celsius * 9 / 5) + 32


t1 = Temperature(20)
t2 = Temperature(30)
t3 = Temperature(20)

print(t1)                      # 20°C
print(repr(t1))                # Temperature(20)
print(t1 == t3)                # True
print(t1 == t2)                # False
print(t1 < t2)                 # True
combined = t1 + t2
print(combined)                # 50°C
print(t1.to_fahrenheit())      # 68.0

temps = [t2, t1, Temperature(25)]
for t in sorted(temps):
    print(t)                   # 20°C, 25°C, 30°C
