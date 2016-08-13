"""
A number sequence generator
"""
__author__ = 'Gareth'


def main():
    x, y = inputs()
    choice = displayChoices("numberSequenceChoices.txt")
    while choice != 6:
        squares = "N"
        print()
        if choice == 1:
            if x % 2 == 1:
                x += 1
                for i in range (x, y, 2):
                    print(i, end=", ")
                x -= 1
            else:
                for i in range (x, y, 2):
                    print(i, end=", ")
        elif choice == 2:
            if x % 2 == 0:
                x += 1
                for i in range (x, y, 2):
                    print(i, end=", ")
                x -= 1
            else:
                for i in range (x, y, 2):
                    print(i, end=", ")
        elif choice == 3:
            for i in range(x, y):
                print(str(i) + " squared is "+ str(i ** i), end=", ")
        elif choice == 4:
            for i in range(1, y):
                if i ** i >= x and i ** i < y:
                    print(str(i) + " squared is "+ str(i ** i), end=", ")
                    squares = "Y"
            if squares == "N":
                print("There are no squares between " + str(x) + " and " + str(y-1) + ".")
        elif choice == 5:
            x, y = inputs()
        else:
            print("An invalid option has been sellected, you entered " + str(choice) + ".")
        print()
        choice = displayChoices("numberSequenceChoices.txt")


    print("Goodbye.")


def inputs():
    x = int(input("Enter the value for \"x\" "))
    y = int(input("Enter the value for \"y\" ")) + 1
    while x >= y:
        print()
        if x == y:
            print("The x value is equal to the y value, please renter the values.")
        else:
            print("The x value is greater then the y value, please reenter the values.")
        x = int(input("Enter the value for \"x\" "))
        y = int(input("Enter the value for \"y\" ")) + 1
    return x, y


def displayChoices(fileName):
    print()
    print()
    choices = open(fileName)
    for line in choices:
        n = line
        print(n, end="")
    choices.close()
    print()
    print()
    choice = int(input("Please select an option. "))
    return choice


if __name__ == "__main__":
    main()