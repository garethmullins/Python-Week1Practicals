"""
A calculator that determins the total cost of shipping.
"""
__author__ = 'Gareth'


def main():
    itemQuantity = []
    itemCost = []
    total = 0
    numItems = int(input("Number of items: "))
    while numItems <= 0:
        print("Invalid Input, expected a possitive number.")
        numItems = int(input("Number of items: "))
    print()
    for i in range (0, numItems):
        print("Item number " + str(i+1), end="\n")
        itemQuantity.append(int(input("Quantity:        ")))
        itemCost.append(int(input("Cost:            ")))
        print()
    for i in range (0, numItems):
        total += itemQuantity[i] * itemCost[i]
    print()
    if total > 100:
        total *= 0.9
    print("Total shipping is:", total)


if __name__ == "__main__":
    main()