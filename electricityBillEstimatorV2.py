"""
Electricity bill estimator V2
"""
__author__ = 'Gareth'


def main():
    print("Electricity bill estimator", end='\n' + '\n')
    tariff = int(input("Which tariff? 11 or 31: "))
    while tariff != 11 and tariff != 31:
        tariff = int(input("An invalid input was entered, please renter the tariff. "))
    if tariff == 11:
        tariff = 0.244618
    else:
        tariff = 0.136928
    daily_use = int(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of billing days: "))
    print()
    bill = 295.01
    print("Estimated bill: $" + str(bill))


if __name__ == "__main__":
    main()