# ---------------------------------------------------------
# DAY 2 | TOPIC 7: DICTIONARIES 📖
# Stores data as KEY → VALUE pairs, like a real dictionary!
# ---------------------------------------------------------


# 1. CREATING A DICTIONARY
# Use curly braces {}. Each item is  "key": value
student = {
    "name"       : "Alice",
    "age"        : 15,
    "city"       : "Kathmandu",
    "is_enrolled": True
}

print(student)


# 2. ACCESSING VALUES — use the KEY (not an index number!)
print("\n--- Reading values ---")
print(student["name"])        # Alice
print(student["age"])         # 15
print(student["city"])        # Kathmandu
print(student["is_enrolled"]) # True


# 3. UPDATING A VALUE
print("\n--- Updating ---")
student["age"] = 16           # happy birthday!
print("New age:", student["age"])


# 4. ADDING A NEW KEY-VALUE PAIR
student["grade"] = "Grade 10"
print("\nAfter adding 'grade':")
print(student)


# 5. REMOVING A KEY
del student["is_enrolled"]
print("\nAfter deleting 'is_enrolled':")
print(student)


# 6. USEFUL DICTIONARY METHODS
print("\n--- Keys, Values, Items ---")
print("Keys  :", list(student.keys()))
print("Values:", list(student.values()))


# 7. REAL-WORLD EXAMPLE: Mini Phone Book
print("\n--- Phone Book ---")
phone_book = {
    "Alice"  : "9841000001",
    "Bob"    : "9841000002",
    "Charlie": "9841000003"
}

name = input("Who do you want to call? ")

if name in phone_book:
    print(f"📞 Calling {name} at {phone_book[name]}...")
else:
    print(f"❌ '{name}' is not in your phone book!")
