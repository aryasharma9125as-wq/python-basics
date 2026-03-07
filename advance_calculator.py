history = []

print("===== Python Calculator =====")

while True:
    print("\nChoose Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Show History")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    if choice == "6":
        print("Calculator closed.")
        break

    if choice == "5":
        print("\nCalculation History:")
        if len(history) == 0:
            print("No calculations yet.")
        else:
            for item in history:
                print(item)
        continue

    if choice in ["1","2","3","4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except:
            print("Invalid input. Please enter numbers.")
            continue

        if choice == "1":
            result = num1 + num2
            operation = f"{num1} + {num2} = {result}"

        elif choice == "2":
            result = num1 - num2
            operation = f"{num1} - {num2} = {result}"

        elif choice == "3":
            result = num1 * num2
            operation = f"{num1} * {num2} = {result}"

        elif choice == "4":
            if num2 == 0:
                print("Error: Division by zero")
                continue
            result = num1 / num2
            operation = f"{num1} / {num2} = {result}"

        print("Result:", result)
        history.append(operation)

    else:
        print("Invalid choice. Try again.")
