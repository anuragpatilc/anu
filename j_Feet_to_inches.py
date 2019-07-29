def main():
    a = float(input('Enter the feet to convert it into inches: '))
    b = feet_to_inches(a)
    print(a, 'foots=', b, 'inches')


def feet_to_inches(a):
    aa = a * 12
    return aa


main()
