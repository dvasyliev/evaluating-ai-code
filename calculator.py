# calculator.py
import math
import operator
from collections import deque

HISTORY_SIZE = 5
MAX_EXPONENT = 100

history = deque(maxlen=HISTORY_SIZE)


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a, b):
    if a == 0 and b < 0:
        raise ValueError("Cannot raise zero to a negative power.")
    if abs(b) > MAX_EXPONENT:
        raise ValueError("Exponent is out of range.")
    try:
        return a ** b
    except OverflowError:
        raise ValueError("Result is too large.")


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)


def percentage(value, percent):
    if percent < 0:
        raise ValueError("Percent cannot be negative.")
    return value * percent / 100


OPERATIONS = {
    "1": ("Add", operator.add),
    "2": ("Subtract", operator.sub),
    "3": ("Multiply", operator.mul),
    "4": ("Divide", divide),
    "5": ("Power", power),
    "6": ("Square root", square_root),
    "7": ("Percentage", percentage),
}

SINGLE_OPERAND = {"6"}

MENU = "\n".join(
    [f"{key}. {name}" for key, (name, _) in OPERATIONS.items()]
    + ["h. History   q. Quit"]
)


def read_number(label):
    raw = input(label).strip()
    if not raw:
        raise ValueError("No number entered.")
    return float(raw)


def read_operands(choice):
    labels = ["First number: "]
    if choice not in SINGLE_OPERAND:
        labels.append("Second number: ")
    return [read_number(label) for label in labels]


def format_history():
    if not history:
        return "No history yet."
    return "\n".join(history)


def main():
    while True:
        print(MENU)
        choice = input("Choose: ").strip().lower()

        if choice == "q":
            break
        if choice == "h":
            print(format_history())
            continue
        if choice not in OPERATIONS:
            print("Unknown option.")
            continue

        name, func = OPERATIONS[choice]
        try:
            result = func(*read_operands(choice))
        except ValueError as e:
            print(f"Error: {e}")
            continue

        print(f"Result: {round(result, 2)}")
        history.append(f"{name}: {result}")


if __name__ == "__main__":
    main()
