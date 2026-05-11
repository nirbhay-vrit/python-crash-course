# ---------------------------------------------------------
# SOLUTION 4: FUNCTIONS CALLING FUNCTIONS 🔧
# ---------------------------------------------------------
# Break a big problem into small helpers. A "driver" function
# orchestrates the helpers to produce the final result.


# TASK 1: Temperature report.
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def is_freezing(c):
    return c <= 0

def temperature_summary(city, celsius):
    f = celsius_to_fahrenheit(celsius)
    k = celsius_to_kelvin(celsius)
    status = "Freezing" if is_freezing(celsius) else "Not freezing"
    print(f"{city} ({celsius}°C): {f}°F | {k}K | {status}")

temperature_summary("London", 15)
temperature_summary("Moscow", -10)
temperature_summary("Phoenix", 45)


# TASK 2: Shopping bill helpers.
def apply_discount(price, percent):
    return price * (1 - percent / 100)

def add_tax(price, tax_rate=0.1):
    return price * (1 + tax_rate)

def format_price(price):
    return f"£{price:.2f}"

def print_item(name, price, discount=0):
    discounted = apply_discount(price, discount)
    with_tax = add_tax(discounted)
    # :<10 → left-align name in a 10-character column for tidy output.
    print(f"{name:<10} → {format_price(with_tax)}")

print_item("Apple", 1.00)
print_item("Bread", 2.00, discount=10)
print_item("Cheese", 5.00, discount=25)


# TASK 3: Word analyser.
def count_words(text):
    return len(text.split())

def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in "aeiou")

def find_longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]   # [::-1] reverses a string

def analyse(text):
    print("\n--- Text analysis ---")
    print(f"Text:           {text}")
    print(f"Word count:     {count_words(text)}")
    print(f"Vowel count:    {count_vowels(text)}")
    longest = find_longest_word(text)
    print(f"Longest word:   {longest}")
    print(f"Is palindrome?: {is_palindrome(longest)}")

analyse("racecar level python programming")


# ⭐ BONUS CHALLENGE: prime tools + number_report.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def number_report(n):
    if is_prime(n):
        print(f"{n} is prime!")
    else:
        factors = prime_factors(n)
        factor_str = ", ".join(str(f) for f in factors)
        print(f"{n} is not prime. Factors: {factor_str}")

number_report(12)
number_report(7)
number_report(60)
