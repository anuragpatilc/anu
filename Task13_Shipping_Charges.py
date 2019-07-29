# Program to calculate the shipping charges of the sales
# Ask the user to enter the quantity to ship
qnt = float(input('Enter the quantity in (pounds) to ship: '))
if qnt <= 2:
    qnt1 = qnt * 1.5
    print('Your total amount to ship your quantity is: $', qnt1, sep='')
else:
    if qnt <= 6:
        qnt2 = qnt * 3
        print('Your total amount to ship your quantity is: $', qnt2, sep='')
    else:
        if qnt <= 10:
            qnt3 = qnt * 4
            print('Your total amount to ship your quantity is: $', qnt3, sep='')
        else:
            qnt4 = qnt * 4.75
            print('Your total amount to ship your quantity is: $', qnt4, sep='')
