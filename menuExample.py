"""
An example of a menu
"""
__author__ = 'Gareth'


def main():
    userName = input("Enter name: ")
    choice = input("(H)ello" + "/n" + "(G)oodbye (Q)uit").upper()
    while choice != "q" and choice != "quit":
        found = "n"
        choices = open('menuChoices.txt')
        for line in choices:
            x = line.split(",")
            if choice == x[0]:
                found = "Y"
                print(x[1] + "/n" + userName)
        choices.close()
        if found == "N":
            print("Invalid choice")
        choice = input("Please enter your choice number, or if you want to quit, enter \"Quit\" ").lower()
    print("Finished")


if __name__ == "__main__":
    main()