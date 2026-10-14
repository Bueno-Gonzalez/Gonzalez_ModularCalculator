#Shows options for operations and asks for users choice then validates
print("Choose a process")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
choice = input(str("Which operation will you choose?(1-4):"))
if choice not in ["1", "2", "3", "4"]:
    print("Invalid input, please choose an operation.")
else:
    #Defines all functions for each operation
    def addition(a, b):
        print("Result is:", a + b)
    
    def subtraction(a, b):
        print("Result is:", a - b)

    def multiplication(a, b):
        print("Result is:", a * b)
    
    def division(a, b):
        if b == 0:
            print("Error, cannot divide by 0")
        else:
            print("Result is:", a / b)
    
        
    #Asks for user values
    num1 = float(input("Insert first number:"))
    num2 = float(input("Insert second number:"))

    #Does operation based on choice
    if choice == "1":
        addition(num1, num2)
    elif choice == "2":
        subtraction(num1, num2)
    elif choice == "3":
        multiplication(num1, num2)
    elif choice == "4":
        division(num1, num2)
