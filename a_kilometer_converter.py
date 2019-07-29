# This program is going to convert the kilometer to miles
def main():
    miles = in_put() * 0.6214

    print('\t\t\t\t', format(miles, ',.2f'))


def in_put():
    kilometer = int(input('Enter the kilometer: '))
    print('kilometer \t\t miles')
    print('----------------------')
    print(kilometer)
    return kilometer


main()
