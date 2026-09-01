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
    if b == 0:
        return "Error: division by zero"
    return a / b


def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        print("Cannot take the square root of a negative number.")
        return None
    return math.sqrt(a)


def percentage(value, percent):
    return value * percent / 100


OPERATIONS = {
    "1": ("Add", add, 2),
    "2": ("Subtract", subtract, 2),
    "3": ("Multiply", multiply, 2),
    "4": ("Divide", divide, 2),
    "5": ("Power", power, 2),
    "6": ("Square root", square_root, 1),
    "7": ("Percentage", percentage, 2),
}


def main():
    while True:
        for key, (name, _, _) in OPERATIONS.items():
            print(f"{key}. {name}")
        print("h. History   q. Quit")

        choice = input("Choose: ").strip().lower()
        if choice == "q":
            break
        if choice == "h":
            print("\n".join(history[-5:]))
            continue
        if choice not in OPERATIONS:
            print("Unknown option.")
            continue

        name, func, arity = OPERATIONS[choice]
        a = float(input("First number: "))
        if arity == 2:
            b = float(input("Second number: "))
            result = func(a, b)
        else:
            result = func(a)
        print(f"Result: {round(result, 2)}")
        history.append(f"{name}: {result}")


main()
