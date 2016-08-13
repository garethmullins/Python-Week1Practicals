"""
A menu
"""
__author__ = 'Gareth'


def main():
    user_name = input("Enter name: ")
    choice = input("Please enter your choice number {}, or if you want to quit, enter \"Quit\" ".format(user_name)).lower()
    while choice != "q" and choice != "quit":
        found = "N"
        choices = open('menuChoices.txt')
        for line in choices:
            x = line.split(",")
            if choice == x[0]:
                found = "Y"
                print(x[1])
        choices.close()
        if found == "N":
            print("An invalid choice has been entered")
        choice = input("Please enter your choice number {}, or if you want to quit, enter \"Quit\" ".format(user_name).lower()
    print("Goodbye{}".format(user_name))


if __name__ == "__main__":
    main()