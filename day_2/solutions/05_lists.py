# ---------------------------------------------------------
# SOLUTION 5: LISTS 📋
# ---------------------------------------------------------


# TASK 1: Favourites List.
# A list holds multiple values in order. Indexing starts at 0.
favourite_movies = ["Inception", "Interstellar", "The Matrix", "Avatar", "Coco"]
print(favourite_movies)
print("First movie:", favourite_movies[0])     # 0 = first
print("Last  movie:", favourite_movies[-1])    # -1 = last


# TASK 2: Add & Remove — lists are MUTABLE (changeable).
favourite_movies.append("Joker")               # adds to the end
favourite_movies.remove("Avatar")              # removes by value
print(favourite_movies)
print("Length:", len(favourite_movies))


# TASK 3: Number List Maths — built-in helpers on numeric lists.
test_scores = [78, 92, 67, 85, 100]
print("Highest:", max(test_scores))
print("Lowest:",  min(test_scores))
print("Total:",   sum(test_scores))
print("Sorted:",  sorted(test_scores))         # returns NEW sorted list


# TASK 4: Indexing Practice.
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"]
print(planets[2])             # 3rd planet = index 2 = Earth
print(planets[-1])            # last planet using negative index
planets[1] = "Saturn"         # replace Venus with Saturn
print(planets)


# ⭐ BONUS CHALLENGE: Shopping List Builder.
# Start empty, then grow the list one .append() at a time.
shopping_list = []
for i in range(3):
    item = input(f"Enter item {i + 1}: ")
    shopping_list.append(item)
print("Your shopping list:", shopping_list)
