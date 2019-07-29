def main():
    aa = float(input('Enter the number of calories that result from fat: '))
    print('calories from fat: ', calories_from_fat(aa))
    bb = float(input('Enter the number of calories that result from carbohydrate: '))
    print('calories from carbohydrates: ', calories_from_carbohydrates(bb))


def calories_from_fat(a):
    b = a * 9
    return b


def calories_from_carbohydrates(b):
    c = b * 4
    return c


main()
