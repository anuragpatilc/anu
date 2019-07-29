def main():
    wall_space = float(input('Enter the wall space to be painted in square feet: '))
    price = float(input('Enter the price of the pant: '))
    a = no_of_gallon(wall_space)
    print('The number of gallons of paint required: ', a, 'gallons')
    b = hour_labor(a)
    print('The hours of labor required: ', b)
    c = a * price
    print('The cost of the paint is: ', c)
    d = labor_charge(b)
    print('The labor charges: ', d)
    total = c + d
    print('The total cost of the paint job is: ', total)


def no_of_gallon(a):
    aa = a / 112
    return aa


def hour_labor(a):
    bb = a * 8
    return bb


def labor_charge(a):
    cc = a * 35
    return cc


main()