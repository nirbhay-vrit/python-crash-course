# ---------------------------------------------------------
# SOLUTION 6: PUTTING IT ALL TOGETHER 🏗️
# Shopping cart project — uses dicts, *args, **kwargs, defaults.
# ---------------------------------------------------------


def create_item(name, price, quantity=1, **extras):
    # Bundle the required fields + whatever extras the caller passed.
    item = {"name": name, "price": price, "quantity": quantity}
    item.update(extras)         # merge in things like organic=True, brand="X"
    return item


def item_total(item):
    return item["price"] * item["quantity"]


def apply_discount(price, percent=0):
    return price * (1 - percent / 100)


def cart_subtotal(*items):
    # Use the accumulator pattern across all passed items.
    total = 0
    for item in items:
        total += item_total(item)
    return total


def add_tax(subtotal, tax_rate=0.1):
    return subtotal * (1 + tax_rate)


def print_receipt(cart_name, *items, discount=0, tax_rate=0.1):
    width = 32
    print("=" * width)
    print(f"  {cart_name}")
    print("=" * width)

    for item in items:
        line_total = item_total(item)
        # Left-align name, right-align numbers for a clean column.
        print(f"  {item['name']:<12} {item['quantity']} x £{item['price']:.2f} "
              f"= £{line_total:.2f}")

    subtotal = cart_subtotal(*items)
    discount_amount = subtotal * discount / 100
    discounted = subtotal - discount_amount
    tax_amount = discounted * tax_rate
    grand_total = discounted + tax_amount

    print("-" * width)
    print(f"  Subtotal:        £{subtotal:.2f}")
    if discount:
        print(f"  Discount ({discount}%):  -£{discount_amount:.2f}")
    print(f"  Tax ({int(tax_rate * 100)}%):        £{tax_amount:.2f}")
    print("=" * width)
    print(f"  TOTAL:           £{grand_total:.2f}")
    print("=" * width)
    return grand_total


# --- Test the cart ---
apple = create_item("Apple", 0.50, quantity=3, organic=True)
bread = create_item("Bread", 1.20, quantity=1)
oj = create_item("Orange Juice", 2.00, quantity=2)
chocolate = create_item("Chocolate", 3.50, quantity=1)

print_receipt("MY SHOPPING CART", apple, bread, oj, chocolate,
              discount=10, tax_rate=0.08)


# ⭐ BONUS CHALLENGE: Compare two carts.
def compare_carts(name_a, items_a, name_b, items_b, discount=0, tax_rate=0.1):
    print(f"\n{'=' * 40}")
    print(f"  CART COMPARISON")
    print(f"{'=' * 40}")
    total_a = print_receipt(name_a, *items_a, discount=discount, tax_rate=tax_rate)
    total_b = print_receipt(name_b, *items_b, discount=discount, tax_rate=tax_rate)

    if total_a < total_b:
        print(f"\n✅ {name_a} is cheaper by £{total_b - total_a:.2f}")
    elif total_b < total_a:
        print(f"\n✅ {name_b} is cheaper by £{total_a - total_b:.2f}")
    else:
        print("\nBoth carts cost the same!")


cart_a = [
    create_item("Pasta", 1.50, quantity=2),
    create_item("Sauce", 2.00, quantity=1),
]
cart_b = [
    create_item("Pizza", 5.00, quantity=1),
    create_item("Soda", 1.00, quantity=2),
]
compare_carts("Cart A (Pasta night)", cart_a,
              "Cart B (Pizza night)", cart_b,
              discount=5, tax_rate=0.08)
