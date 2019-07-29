def main():
    tax = int(input('Enter the total property valuation: '))
    a = tax_coll(tax)
    print('The assessment value is: ', tax_coll(tax))
    print('The property tax is: ', format(acre(a), ',.2f'))


def tax_coll(a):
    b = a * 0.60
    return b


def acre(a):
    c = (a / 100) * 0.72
    return c


main()
