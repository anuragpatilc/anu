def main():
    price = int(input('Enter the replacement cost of the building: '))
    print('Minimum price of insurance he or she should bye for the property is: ', calculating_insurance(price))


def calculating_insurance(a):
    b = a * 0.80
    return b


main()
