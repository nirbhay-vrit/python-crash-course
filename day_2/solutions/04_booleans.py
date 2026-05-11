# ---------------------------------------------------------
# SOLUTION 4: BOOLEANS, type(), AND TYPE CONVERSION ✅❌
# ---------------------------------------------------------


# TASK 1: Boolean variables — only two possible values: True or False.
do_you_like_music = True
do_you_have_a_pet = False
do_you_like_mornings = True
do_you_drink_coffee = True

print(f"Do I like music?      {do_you_like_music}")
print(f"Do I have a pet?      {do_you_have_a_pet}")
print(f"Do I like mornings?   {do_you_like_mornings}")
print(f"Do I drink coffee?    {do_you_drink_coffee}")


# TASK 2: Comparison operators — each one returns True or False.
age = 18
print(age == 18)   # True   (== means "is equal to")
print(age > 20)    # False  (18 is not greater than 20)
print(age < 21)    # True
print(age != 15)   # True   (!= means "is not equal to")
print(age >= 18)   # True   (>= means "greater than or equal to")


# TASK 3: type() Detective — shows the data type of any value.
my_string = "hello"
my_int = 42
my_float = 3.14
my_bool = True
print(f"Value: {my_string}    Type: {type(my_string)}")
print(f"Value: {my_int}       Type: {type(my_int)}")
print(f"Value: {my_float}     Type: {type(my_float)}")
print(f"Value: {my_bool}      Type: {type(my_bool)}")


# TASK 4: Type Conversion + Input.
birth_year = int(input("What year were you born? "))
age = 2024 - birth_year
print(f"You are approximately {age} years old!")


# ⭐ BONUS CHALLENGE: a comparison directly inside print().
score = int(input("Enter your exam score (0–100): "))
print(score >= 40)
