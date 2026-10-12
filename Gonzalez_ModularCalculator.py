#Shows options for operations and asks for users choice
print("Choose a process")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
choice = input(str("Which operation will you choose?(1-4):"))

#Defines all functions for each operation
def addition(a, b):
    add_answer = (a + b)
    print("Result is:", add_answer)
            
def subtraction(a, b):
    sub_answer = (a - b)
    print("Result is:", sub_answer)
            
def multiplication(a, b):
    mul_answer = (a * b)
    print("Result is:", mul_answer)
            
def division(a, b):
    div_answer = (a / b)
    print("Result is:", div_answer)
        
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
