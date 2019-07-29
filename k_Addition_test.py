import random


def main():
    print('Q1')
    a, b = rand()
    aa = a + b
    print(aa)
    print()
    print('Q2')
    a, b = rand()
    bb = a + b
    print(bb)
    print()
    print('Q3')
    a, b = rand()
    cc = a + b
    print(cc)
    print()
    print('Q4')
    a, b = rand()
    dd = a + b
    print(dd)
    print()
    print('Q5')
    a, b = rand()
    ee = a + b
    print(ee)
    print()


def rand():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return a, b


main()
