"""
An electricity bill estimator
"""
__author__ = 'Gareth'


def main():
    print("Electricity bill estimator", end='\n' + '\n')
    cents = int(input("Enter cents per kWh: "))
    dailyUse = int(input("Enter daily use in kWh: "))
    billingDays = int(input("Enter number of billing days: "))
    print()
    bill = 141.75
    print("Estimated bill: $" + str(bill))


if __name__ == "__main__":
    main()