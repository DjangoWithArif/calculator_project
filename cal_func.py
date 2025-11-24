
# Addition function
def add(a,b):
    return a + b

# Subtraction function
def sub(a,b):
    return a - b

# Multipication function
def mul(a,b):
    return a * b

# Division function
def divided(a,b):
    if b == 0:
        return "Can't devided by Zero."
    return a // b

# for better user experience menu
def show_menu():
    print("\n" + "=" * 40)
    print("==== Basic Calculator ====")
    print("Press 1. Add")
    print("Press 2. Subtract")
    print("Press 3. Multipli")
    print("Press 4. Devide")
    print("Press 5. Exit")
    print("=" * 40)
