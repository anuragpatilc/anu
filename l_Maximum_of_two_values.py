def main():
    a, b = two_in()
    if a > b:
        print('largest number is: ', a)
        print('Smallest number is: ', b)
    else:
        print('largest number is: ', b)
        print('Smallest number is: ', a)


def two_in():
    a = float(input('Enter the number: '))
    b = float(input('Enter the number: '))
    return a, b


main()
