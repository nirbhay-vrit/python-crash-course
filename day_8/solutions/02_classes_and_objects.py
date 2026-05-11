# ---------------------------------------------------------
# SOLUTION 2: CLASSES AND OBJECTS
# ---------------------------------------------------------


# EXERCISE 1: First class — Phone.
# `pass` is a placeholder body so Python doesn't error on an empty class.
# We then attach attributes one-by-one to each object via dot notation.
class Phone:
    pass

phone1 = Phone()
phone1.brand = "Samsung"
phone1.colour = "black"
phone1.price = 30000

phone2 = Phone()
phone2.brand = "Apple"
phone2.colour = "white"
phone2.price = 80000

phone3 = Phone()
phone3.brand = "OnePlus"
phone3.colour = "blue"
phone3.price = 25000

for p in (phone1, phone2, phone3):
    print(f"Brand: {p.brand}, Colour: {p.colour}, Price: {p.price}")


# EXERCISE 2: type() and isinstance().
class Laptop:
    pass

lp1 = Laptop()
lp2 = Laptop()
lp1.brand = "Dell"
lp2.brand = "HP"

print(type(lp1))                  # → <class '__main__.Laptop'>
print(type(lp2))                  # → <class '__main__.Laptop'>
print(isinstance(lp1, Laptop))    # → True
print(isinstance(42, Laptop))     # → False
print(lp1 == lp2)                 # → False (no __eq__ defined, so identity check)
print(lp1 is lp2)                 # → False (two distinct objects in memory)


# EXERCISE 3: Create + modify Superhero.
class Superhero:
    pass

batman = Superhero()
batman.name = "Batman"
batman.power = "Gadgets"
batman.city = "Gotham"
print(f"{batman.name} — {batman.power} — {batman.city}")

batman.city = "Metropolis"        # change the attribute on an existing object
print(f"{batman.name} — {batman.power} — {batman.city}")


# EXERCISE 4: Mini inventory.
class FruitItem:
    pass

apple = FruitItem()
apple.name = "Apple"
apple.price_per_kg = 200
apple.stock_kg = 10

banana = FruitItem()
banana.name = "Banana"
banana.price_per_kg = 80
banana.stock_kg = 25

mango = FruitItem()
mango.name = "Mango"
mango.price_per_kg = 350
mango.stock_kg = 8

grape = FruitItem()
grape.name = "Grape"
grape.price_per_kg = 500
grape.stock_kg = 5

inventory = [apple, banana, mango, grape]
for fruit in inventory:
    print(f"{fruit.name}: Rs. {fruit.price_per_kg}/kg, stock: {fruit.stock_kg}kg")
