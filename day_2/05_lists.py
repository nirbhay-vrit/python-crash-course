# ---------------------------------------------------------
# DAY 2 | TOPIC 5: LISTS 📋
# A list stores MULTIPLE values in ONE variable!
# ---------------------------------------------------------


# 1. CREATING A LIST
# Use square brackets []. Separate items with commas.
fruits = ["apple", "banana", "mango", "orange"]
scores = [95, 87, 72, 100, 65]
mixed  = ["Alice", 15, True, 3.14]   # lists can hold any types!

print(fruits)
print(scores)
print(mixed)


# 2. ACCESSING ITEMS — Indexing starts at ZERO!
#
#   fruits  = ["apple",  "banana",  "mango",  "orange"]
#   index      [  0  ]   [  1   ]   [  2  ]   [  3  ]
#
print("\n--- Indexing ---")
print(fruits[0])    # apple   ← first item
print(fruits[1])    # banana
print(fruits[2])    # mango
print(fruits[-1])   # orange  ← -1 always means the LAST item
print(fruits[-2])   # mango   ← -2 is second from last


# 3. LIST LENGTH
print("\nNumber of fruits:", len(fruits))


# 4. CHANGING AN ITEM
print("\n--- Updating a list ---")
print("Before:", fruits)
fruits[1] = "grape"              # replace "banana" with "grape"
print("After :", fruits)


# 5. ADDING & REMOVING ITEMS
print("\n--- Adding & Removing ---")
fruits.append("watermelon")      # append adds to the END
print("After append:", fruits)

fruits.remove("apple")           # remove the first match
print("After remove:", fruits)


# 6. USEFUL LIST FUNCTIONS
numbers = [5, 3, 9, 1, 7, 4]
print("\n--- Useful functions ---")
print("List    :", numbers)
print("Max     :", max(numbers))
print("Min     :", min(numbers))
print("Sum     :", sum(numbers))
print("Sorted  :", sorted(numbers))   # returns a NEW sorted list
print("Length  :", len(numbers))
