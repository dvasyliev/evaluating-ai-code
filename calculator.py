# calculator.py
import math

history = []


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def power(a, b):
    return a ** b


def square_root(a, b=None):
    if math.sign(a) < 0:
        print("Cannot take the square root of a negative number.")
        return None
    return math.sqrt(a)


def percentage(value, percent):
    return value / percent * 100


def save_history():
    with open("history.txt", "w") as f:
        f.write("\n".join(history))
    print("History saved to history.txt")


OPERATIONS = {
    "1": ("Add", add),
    "2": ("Subtract", subtract),
    "3": ("Multiply", multiply),
    "4": ("Divide", divide),
    "5": ("Power", power),
    "6": ("Square root", square_root),
    "7": ("Percentage", percentage),
}


def main():
    while True:
        for key, (name, _) in OPERATIONS.items():
            print(f"{key}. {name}")
        print("h. History   q. Quit")

        choice = input("Choose: ").strip().lower()
        if choice == "q":
            save_history()
            break
        if choice == "h":
            print("\n".join(history[-5:]))
            continue
        if choice not in OPERATIONS:
            print("Unknown option.")
            continue

        name, func = OPERATIONS[choice]
        a = float(input("First number: "))
        b = float(input("Second number: "))
        result = func(a, b)
        print(f"Result: {result}")
        history.append(f"{name}: {a}, {b} = {result}")


main()
