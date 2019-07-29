def main():
    a, b, c, d, e, f = operations_automobiles()
    tot = a + b + c + d + e + f
    print('The monthly expensive of the automobile is: ', tot)


def main1():
    k = 0
    for x in range(1, 12):
        if x == 1:
            print('january')
        elif x == 2:
            print('February')
        elif x == 3:
            print('March')
        elif x == 4:
            print('April')
        elif x == 5:
            print('May')
        elif x == 6:
            print('June')
        elif x == 7:
            print('July')
        elif x == 8:
            print('August')
        elif x == 9:
            print('September')
        elif x == 10:
            print('October')
        elif x == 11:
            print('November')
        else:
            print('December')

        a, b, c, d, e, f = operations_automobiles()
        tot = a + b + c + d + e + f
        k = k + tot
    print('The annual expensive of the automobile is:', k)


def operations_automobiles():
    a = float(input('Enter the loan amount for this month: '))
    b = float(input('Enter the insurance cost of this month: '))
    c = float(input('Enter the total gas cost of this month: '))
    d = float(input('Enter the total oil cost of this month: '))
    e = float(input('Enter the total tires cost of this month:'))
    f = float(input('Enter the total maintenance cost of this month: '))
    return a, b, c, d, e, f


print('Do u want one mont computation or one year computation month = 1 and year = 2: ', end='')
key = int(input())
if key == 1:
    import datetime
    time = datetime.datetime.today()
    print(f"{time:%d %b, %y}")
    main()
else:
    main1()
