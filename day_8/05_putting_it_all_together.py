# ---------------------------------------------------------
# DAY 8 | TOPIC 5: PUTTING IT ALL TOGETHER
# Two complete mini-projects using: class, __init__, methods, objects.
# ---------------------------------------------------------


# ═══════════════════════════════════════════════════════════
# MINI PROJECT 1: STUDENT GRADE TRACKER
# ═══════════════════════════════════════════════════════════

class Student:
    def __init__(self, name, roll_number):
        self.name        = name
        self.roll_number = roll_number
        self.scores      = []   # starts empty; filled by add_score()

    def add_score(self, subject, score):
        self.scores.append({"subject": subject, "score": score})

    def get_average(self):
        if len(self.scores) == 0:
            return 0
        total = sum(item["score"] for item in self.scores)
        return total / len(self.scores)

    def get_grade(self):
        avg = self.get_average()      # calls another method
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "F"

    def report(self):
        print(f"\n  ── {self.name}  (Roll #{self.roll_number}) ──")
        for item in self.scores:
            print(f"    {item['subject']:<12} : {item['score']}")
        print(f"    {'Average':<12} : {self.get_average():.1f}")
        print(f"    {'Grade':<12} : {self.get_grade()}")


print("=" * 50)
print("  STUDENT GRADE TRACKER")
print("=" * 50)

alice   = Student("Alice",   101)
bob     = Student("Bob",     102)
charlie = Student("Charlie", 103)

alice.add_score("Maths",   88)
alice.add_score("English", 92)
alice.add_score("Science", 79)

bob.add_score("Maths",   65)
bob.add_score("English", 70)
bob.add_score("Science", 58)

charlie.add_score("Maths",   95)
charlie.add_score("English", 91)
charlie.add_score("Science", 97)

for student in [alice, bob, charlie]:
    student.report()


# ═══════════════════════════════════════════════════════════
# MINI PROJECT 2: SIMPLE PRODUCT INVENTORY
# ═══════════════════════════════════════════════════════════

class Product:
    def __init__(self, name, price, stock):
        self.name  = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        if quantity > self.stock:
            print(f"  Cannot sell {quantity} × {self.name}. Only {self.stock} left.")
        else:
            self.stock -= quantity
            print(f"  Sold {quantity} × {self.name}. Remaining stock: {self.stock}")

    def restock(self, quantity):
        self.stock += quantity
        print(f"  Restocked {self.name} by {quantity}. New stock: {self.stock}")

    def info(self):
        print(f"  {self.name:<15} | Price: Rs.{self.price:>7.2f} | Stock: {self.stock}")


print("\n\n" + "=" * 50)
print("  PRODUCT INVENTORY")
print("=" * 50)

apple  = Product("Apple",  0.50,  100)
banana = Product("Banana", 0.30,  80)
mango  = Product("Mango",  1.20,  30)

print("\n  --- Initial Inventory ---")
for p in [apple, banana, mango]:
    p.info()

print("\n  --- Transactions ---")
apple.sell(20)
banana.sell(100)    # more than stock — blocked!
mango.restock(50)

print("\n  --- Updated Inventory ---")
for p in [apple, banana, mango]:
    p.info()


# ─────────────────────────────────────────────────────────
# WHAT WE USED TODAY — Quick Recap
# ─────────────────────────────────────────────────────────
# ✅ class      — defined a blueprint
# ✅ __init__   — constructor, sets up every object the same safe way
# ✅ self       — the specific object being used; connects attributes to it
# ✅ attributes — data stored on each object (self.name, self.scores)
# ✅ methods    — functions belonging to the class (add_score, report)
# ✅ objects    — alice, bob, apple, mango — all independent instances
