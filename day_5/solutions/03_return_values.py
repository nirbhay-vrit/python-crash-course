# ---------------------------------------------------------
# SOLUTION 3: RETURN VALUES 📤
# ---------------------------------------------------------
# `return` sends a value OUT of the function so the caller can use it.
# print() shows something on screen — return GIVES BACK a value.


# TASK 1: Multiply.
def multiply(a, b):
    return a * b

print(multiply(4, 5))           # 20


# TASK 2: Find max of two numbers (without using built-in max()).
def find_max(x, y):
    if x >= y:
        return x
    return y                    # only reached when y > x

print(find_max(10, 5))          # 10
print(find_max(3, 8))           # 8
print(find_max(7, 7))           # 7


# TASK 3: Repeat string n times.
def repeat_string(text, times):
    return text * times

print(repeat_string("*", 5))    # *****
print(repeat_string("Na", 4))   # NaNaNaNa


# TASK 4: Using return in an expression.
def square(n):
    return n * n

print(square(3) + square(4))    # 9 + 16 = 25


# ⭐ BONUS CHALLENGE: is_prime.
# A prime > 1 has no divisor other than 1 and itself.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):       # check 2..n-1
        if n % i == 0:
            return False        # found a divisor → not prime
    return True

for n in [2, 4, 7, 9, 17]:
    print(n, "→", is_prime(n))
