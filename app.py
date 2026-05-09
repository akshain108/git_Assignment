#!/usr/bin/env python3
"""Simple calculator with addition and subtraction."""

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

def percentage(a, b):
    if b == 0:
        raise ValueError("Cannot calculate percentage with zero.")
    return (a / b) * 100

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("Calculator: addition, subtraction, multiplication, and division")
    while True:
        print("\nChoose an option:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Percentage")
        print("6. Exit")

        choice = input("Enter 1, 2, 3, 4, 5, or 6: ").strip()
        if choice == "6":
            print("Thank you, See you again Bye")
            break
        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Invalid choice. Try again.")
            continue

        x = get_number("Enter the first number: ")
        y = get_number("Enter the second number: ")

        if choice == "1":
            result = add(x, y)
            op = "+"
        elif choice == "2":
            result = subtract(x, y)
            op = "-"
        elif choice == "3":
            result = multiply(x, y)
            op = "*"
        elif choice == "4":
            result = divide(x, y)
            op = "/"
        elif choice == "5":
            result = percentage(x, y)
            op = "%"
        else:
            print("Invalid choice. Try again.")
            continue
        print(f"{x} {op} {y} = {result}")


if __name__ == "__main__":
    main()
