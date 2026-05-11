# ---------------------------------------------------------
# SOLUTION 2: range() 🔢
# ---------------------------------------------------------
# range(start, stop, step) — `stop` is EXCLUDED. step defaults to 1.


# TASK 1: Multiplication Table (1 to 12).
number = int(input("Enter a number: "))
for i in range(1, 13):          # 1..12
    print(f"{number} × {i} = {number * i}")


# TASK 2: Sum of numbers in a user-given range.
start = int(input("Start: "))
end = int(input("End: "))
total = 0
for n in range(start, end + 1): # +1 so the END value is INCLUDED
    total += n
print(f"Sum from {start} to {end}: {total}")


# TASK 3: Rocket Countdown — negative step counts DOWN.
for i in range(10, 0, -1):      # 10, 9, 8, ... 1
    print(i)
print("Liftoff! 🚀")


# ⭐ BONUS CHALLENGE: Numbers divisible by BOTH 3 and 7.
# "Divisible by both" = divisible by 21, but we'll check both to be clear.
for n in range(1, 101):
    if n % 3 == 0 and n % 7 == 0:
        print(n)
