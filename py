def add(x, y):
    return x + y
    def subtract(x, y):
    return x - y
    def multiply(x, y):
    return x * y
    def divide(x, y):
    return x / y
    print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
