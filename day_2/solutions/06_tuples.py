# ---------------------------------------------------------
# SOLUTION 6: TUPLES 🔒
# ---------------------------------------------------------
# A tuple is like a list, but IMMUTABLE — once made, it can't be changed.
# Use () instead of [] to create one.


# TASK 1: Favourite colours tuple.
top_5_colors = ("blue", "green", "red", "purple", "yellow")
print(top_5_colors)
print(top_5_colors[0])   # first colour
print(top_5_colors[2])   # third colour (index starts at 0)


# TASK 2: Indexing & length.
print(top_5_colors[-1])         # last colour (negative index)
print(len(top_5_colors))        # how many items in the tuple


# TASK 3: Spot the difference.
my_list  = [1, 2, 3]
my_tuple = (1, 2, 3)

my_list.append(4)               # ✅ works — lists are mutable
print(my_list)

# my_tuple.append(4)            # ❌ AttributeError — tuples have no .append()
# my_tuple[0] = 99              # ❌ TypeError      — you can't modify a tuple
# Tuples are immutable: once created, their contents are locked.


# TASK 4: Tuple Unpacking.
# You can assign multiple variables in one line by matching the tuple's shape.
person = ("Bibek", 25, "Kathmandu")
name, age, city = person
print(f"Hi! I'm {name}, {age} years old, from {city}.")


# ⭐ BONUS CHALLENGE: The 12 months.
months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")
print("First:", months[0])
print("Last: ", months[-1])
print("Total:", len(months))
print("Index 6:", months[6])   # → July (because index 0 is January)
