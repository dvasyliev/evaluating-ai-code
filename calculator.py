# calculator.py

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


def main():
    a = float(input("First number: "))
    b = float(input("Second number: "))
    print("Sum:", add(a, b))


main()
