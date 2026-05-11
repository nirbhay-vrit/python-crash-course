# ---------------------------------------------------------
# SOLUTION 1: VARIABLES 📦
# ---------------------------------------------------------


# TASK 1: Personal details stored in variables.
# A variable is just a labelled "box" that holds a value.
your_name = "Bibek"
your_age = 25
your_favorite_color = "Blue"
your_country = "Nepal"
your_hobby = "Reading"


# TASK 2: Profile card — we re-use the variables (don't retype the value).
# str(your_age) is needed because + can't mix numbers and strings.
print("╔══════════════════════════╗")
print("║      MY PROFILE CARD     ║")
print("╠══════════════════════════╣")
print("  Name:    " + your_name)
print("  Age:     " + str(your_age))
print("  Color:   " + your_favorite_color)
print("  Country: " + your_country)
print("  Hobby:   " + your_hobby)
print("╚══════════════════════════╝")


# TASK 3: Re-assign the variable to next year's age.
# Variables can change — that's why they are called "variable" 🙂
your_age = your_age + 1   # or: your_age += 1
print("Next year, I will be " + str(your_age) + " years old!")


# TASK 4: Greeting — combine two variables in one sentence.
print("Hello! I am " + your_name + " from " + your_country + ".")


# ⭐ BONUS CHALLENGE:
# Three new variables, then one creative sentence.
favourite_drink = "coffee"
dream_place = "Tokyo"
lucky_number = 7
print("If I had " + str(lucky_number) + " cups of " + favourite_drink
      + ", I'd hop on a plane to " + dream_place + " tonight!")
