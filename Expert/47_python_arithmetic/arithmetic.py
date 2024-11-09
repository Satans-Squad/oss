# arithmetic.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

def main():
    print("Enter first number: ")
    x = float(input())
    print("Enter second number: ")
    y = float(input())

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    operation = input("Enter operation (1/2/3/4): ")

    if operation == '1':
        print(f"Result: {add(x, y)}")
    elif operation == '2':
        print(f"Result: {subtract(x, y)}")
    elif operation == '3':
        print(f"Result: {multiply(x, y)}")
    elif operation == '4':
        print(f"Result: {divide(x, y)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
