# ---------------------------------------------------------
# SOLUTION 7: DICTIONARIES 📖
# ---------------------------------------------------------
# A dictionary stores KEY → VALUE pairs. Great for labelled data.


# TASK 1: Profile dictionary.
my_profile = {
    "name": "Bibek",
    "age": 25,
    "city": "Kathmandu",
    "hobby": "Reading",
    "favorite_food": "Momo",
}
print(my_profile)
print(my_profile["hobby"])      # look up a value by its key


# TASK 2: Update & add.
my_profile["age"] = my_profile["age"] + 1            # update existing key
my_profile["favourite_subject"] = "Mathematics"      # add a brand-new key
print(my_profile)


# TASK 3: Keys and values.
print(my_profile.keys())        # dict_keys([...])
print(my_profile.values())      # dict_values([...])


# TASK 4: Country Capital look-up.
# The `in` operator checks if a key exists in the dictionary.
capitals = {
    "Nepal": "Kathmandu",
    "India": "New Delhi",
    "Japan": "Tokyo",
    "France": "Paris",
    "Brazil": "Brasília",
}
country = input("Type a country name: ")
if country in capitals:
    print(f"The capital of {country} is {capitals[country]}")
else:
    print("Country not found!")


# ⭐ BONUS CHALLENGE: Simple Grade Book.
grades = {"Maths": 92, "Science": 88, "English": 76, "History": 84, "Art": 95}

for subject, score in grades.items():       # .items() gives (key, value) pairs
    print(f"{subject}: {score}")

highest_score = max(grades.values())
# Find which subject hit that score — loop through and compare.
for subject, score in grades.items():
    if score == highest_score:
        print(f"Highest score is in {subject} ({score})")
        break
