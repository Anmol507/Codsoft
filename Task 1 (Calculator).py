import sys

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y
    
print("This is a Simple Arithmetic Calculator Made by Anmol using Python Programming")
    
while True:
    print("*************************************************************************")
    print("Press 1. for Addition")
    print("Press 2. for Subtraction")
    print("Press 3. for Multiplication")
    print("Press 4. for Division")
    print("Press 0. to Exit")

    choice = int(input("Please Enter your choice: "))

    if choice not in (1, 2, 3, 4, 0):
        print("Invalid input")
    else:
        if (choice == 0):
            print("Program has been Successfully terminated")
            sys.exit()
        else:
            n1 = float(input("Please enter the first number: "))
            n2 = float(input("Please enter the second number: "))

            if choice == 1:
                print(f"Addition of {n1} , {n2} is: ", addition(n1, n2))
            elif choice == 2:
                print(f"Subtraction of {n1} , {n2} is: ", subtraction(n1, n2))
            elif choice == 3:
                print(f"Multiplication of {n1}, {n2} is: ", multiplication(n1, n2))
            elif choice == 4:
                if n2 == 0:
                    print("Cannot divide by zero")
                else:
                    print(f"Divison of {n1} , {n2} is: ", division(n1, n2))
        
