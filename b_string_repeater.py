def main():
    print(cal())


def cal():
    c = name() * times()
    return c


def name():
    a = input('Enter the name: ')
    return a


def times():
    b = int(input('Enter the times: '))
    return b


main()
