# calculator.py
import math

history = []
MAX_EXPONENT = 100


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a, b):
    if a == 0 and b < 0:
        raise ValueError("Cannot raise zero to a negative power.")
    if abs(b) > MAX_EXPONENT:
        raise ValueError("Exponent is out of range.")
    return a ** b


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)


def percentage(value, percent):
    return value * percent / 100


def read_number(label):
    raw = input(label).strip()
    if not raw:
        raise ValueError("No number entered.")
    return float(raw)


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
            if not history:
                print("No history yet.")
            else:
                print("\n".join(history[-5:]))
            continue
        if choice not in OPERATIONS:
            print("Unknown option.")
            continue

        name, func, arity = OPERATIONS[choice]
        try:
            a = read_number("First number: ")
            if arity == 2:
                b = read_number("Second number: ")
                result = func(a, b)
            else:
                result = func(a)
        except ValueError as e:
            print(f"Error: {e}")
            continue
        print(f"Result: {round(result, 2)}")
        history.append(f"{name}: {result}")


main()
