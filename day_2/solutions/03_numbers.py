# ---------------------------------------------------------
# SOLUTION 3: NUMBERS 🔢
# ---------------------------------------------------------


# TASK 1: Rectangle Maths.
length = 8
width = 5
area = length * width                # multiplication
perimeter = 2 * (length + width)     # parentheses control order of operations
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")


# TASK 2: Floor division (//) gives the whole-number part of a division.
# Modulus (%) gives the remainder — exactly what's "left over".
total_candies = 47
friends = 5
each = total_candies // friends      # 47 // 5  → 9
leftover = total_candies % friends   # 47 %  5  → 2
print(f"Each friend gets {each} candies, with {leftover} left over!")


# TASK 3: User Input Calculator.
# input() returns a string, so we must wrap it with int() to do maths.
a = int(input("Enter first whole number: "))
b = int(input("Enter second whole number: "))
print(f"Sum:        {a + b}")
print(f"Difference: {a - b}")
print(f"Product:    {a * b}")
print(f"Quotient:   {a / b}")        # / always gives a float (e.g. 7 / 2 = 3.5)


# TASK 4: Price Calculator — float() lets us handle decimals like 9.99.
items = int(input("How many items do you want to buy? "))
price = float(input("Price per item: "))
total = items * price
print(f"Total cost: {total}")


# ⭐ BONUS CHALLENGE: Temperature Converter.
celsius = float(input("Temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")
