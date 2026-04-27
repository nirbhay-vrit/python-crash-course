# ---------------------------------------------------------
# DAY 2 | TOPIC 3: NUMBERS 🔢
# Python has two numeric types: int (whole) and float (decimal)
# ---------------------------------------------------------


# 1. INTEGERS (int) — Whole numbers, no decimal point
students = 30
high_score = 9500
birth_year = 2009

print("Students in class:", students)
print("High score:", high_score)
print("Birth year:", birth_year)


# 2. FLOATS (float) — Numbers with a decimal point
price = 9.99
body_temp = 36.6
pi = 3.14159

print("\nPrice: Rs.", price)
print("Body temperature:", body_temp, "°C")
print("Pi is approximately:", pi)


# 3. ALL THE ARITHMETIC OPERATORS
a = 20
b = 6

print(f"\n--- Math with {a} and {b} ---")
print(f"Addition       {a} + {b}  = {a + b}")
print(f"Subtraction    {a} - {b}  = {a - b}")
print(f"Multiplication {a} * {b}  = {a * b}")
print(f"Division       {a} / {b}  = {a / b}")    # always gives a float!
print(f"Floor Division {a} // {b} = {a // b}")   # whole-number result (rounds down)
print(f"Modulus        {a} % {b}  = {a % b}")    # remainder after dividing
print(f"Exponent       {a} ** 2   = {a ** 2}")   # 20 squared


# 4. REAL-WORLD MATH EXAMPLE
print("\n--- Shopping Receipt ---")
item_price = 250
quantity = 4
discount = 50

subtotal = item_price * quantity
final_price = subtotal - discount

print(f"Price per item : Rs. {item_price}")
print(f"Quantity       : {quantity}")
print(f"Subtotal       : Rs. {subtotal}")
print(f"Discount       : Rs. {discount}")
print(f"Final Price    : Rs. {final_price}")


# 5. INPUT WITH NUMBERS
# Remember: input() always gives us a STRING!
# We MUST convert it with int() or float() to do any math.
print("\n--- Mini Calculator ---")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number: "))

print(f"\n{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} × {num2} = {num1 * num2}")
print(f"{num1} ÷ {num2} = {num1 / num2}")


# 6. ROUNDING
messy_result = 10 / 3
print(f"\n10 ÷ 3 = {messy_result}")
print(f"Rounded to 2 decimal places: {round(messy_result, 2)}")
