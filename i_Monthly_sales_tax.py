def main():
    a = float(input('Enter the total sales for the month (amount): '))
    b = state_tac(a)
    c = country_tax(a)
    tot = b + c
    print('The amount of country sales tax is: ', c)
    print('The amount of state sales tax is:', b)
    print('The total sales rax( country and state)', tot)


def state_tac(a):
    aa = a * 0.05
    return aa


def country_tax(a):
    bb = a * 0.025
    return bb


main()
