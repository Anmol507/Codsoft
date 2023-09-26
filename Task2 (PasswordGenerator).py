import random
import array

Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

LowerCh = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

UpperCh = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

Symbols= ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

def GenPass(length):
    characters = LowerCh + UpperCh + Digits + Symbols
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

def main():
    try:
        print("This is a Password Generator made by Anmol using Python Programming")
        print("*******************************************************************")
        length = int(input("Please enter the length of your desired password: "))
        if length <= 0:
            print("OOPS!! Length must be greater than 0, Please enter valid length")
            return
        result = GenPass(length)
        print("Generated Password: ", result)

    except ValueError:
        print("Please enter a Positive Integer of valid length.")

if __name__ == "__main__":
    main()

