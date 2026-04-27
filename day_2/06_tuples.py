# ---------------------------------------------------------
# DAY 2 | TOPIC 6: TUPLES 🔒
# Like a list, but LOCKED — the items can never be changed!
# ---------------------------------------------------------


# 1. CREATING A TUPLE
# Use round brackets () instead of square brackets []
coordinates  = (27.7172, 85.3240)      # Kathmandu GPS
rgb_red      = (255, 0, 0)             # red colour in RGB
days_of_week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

print(coordinates)
print(rgb_red)
print(days_of_week)


# 2. ACCESSING ITEMS — exactly the same as lists!
print("\n--- Indexing ---")
print(days_of_week[0])    # Mon   (index 0 = first)
print(days_of_week[-1])   # Sun   (index -1 = last)
print(days_of_week[4])    # Fri


# 3. TUPLE LENGTH
print("\nNumber of days:", len(days_of_week))


# 4. TUPLES ARE IMMUTABLE (cannot be changed!)
# Try uncommenting the line below to see the error:
# days_of_week[0] = "Monday"    # ← TypeError! Tuples are locked.

print("\nTuples are safe — nobody can accidentally change them!")


# 5. UNPACKING — assign each item to its own variable
print("\n--- Unpacking ---")
latitude, longitude = coordinates
print(f"Latitude : {latitude}")
print(f"Longitude: {longitude}")

red, green, blue = rgb_red
print(f"Red={red}  Green={green}  Blue={blue}")


# 6. WHEN TO USE TUPLE vs LIST?
#
#   LIST  → use when data will change  (shopping list, scores, etc.)
#   TUPLE → use when data stays fixed  (coordinates, RGB, weekdays)
#
print("\n--- List vs Tuple ---")
shopping = ["milk", "eggs", "bread"]     # list  — will grow/shrink
point    = (10, 20)                       # tuple — fixed 2D point

shopping.append("butter")   # ✅ works fine
print(shopping)
# point[0] = 99             # ❌ would crash — tuples are immutable
print(point)
