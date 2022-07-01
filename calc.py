# imports

# global

# functions
def print_menu():
    print("-----------------")
    print("    PyCal3000")
    print("-----------------")

    print("[1] Sum")
    print("[2] Substract")
    print("[3] Multiply")
    print("[4] Divide")
    print()
    print("[E] Exit")
    print()


# plain instructions
option = ""

while option != "E":
    print_menu()
    option = input("Please select and option: ")
    if option == "E" or option == "e":
        break
    print()

    num1 = float(input("Please provide number one: "))
    num2 = float(input("Please provide number two: "))

    if option == "1":
        total = num1 + num2

    elif option == "2":
        total = num1 - num2

    elif option == "3":
        total = num1 * num2

    elif option == "4":
        if num2 == 0:
            print("Be careful!")
            total = ("Error: Zero division not allowed")
        else:
            total = num1 / num2

    print("The result is: " + str(total))
    print()
    print("Press Enter to continue...")
    print()

print("Thank you, good bye!")
