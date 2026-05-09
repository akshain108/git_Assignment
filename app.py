#!/usr/bin/env python3
"""Simple calculator with addition and subtraction."""

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("Calculator: addition and subtraction")
    while True:
        print("\nChoose an option:")
        print("1. Add")
        print("2. Subtract")
        print("3. Exit")

        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == "3":
            print("Goodbye!")
            break
        if choice not in {"1", "2"}:
            print("Invalid choice. Try again.")
            continue

        x = get_number("Enter the first number: ")
        y = get_number("Enter the second number: ")

        if choice == "1":
            result = add(x, y)
            op = "+"
        else:
            result = subtract(x, y)
            op = "-"

        print(f"{x} {op} {y} = {result}")


if __name__ == "__main__":
    main()
