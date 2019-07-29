# Program to determine to discount Software sales
soft = int(input('Enter the quantity of software you purchased: '))
soft1 = soft * 99
print('Your total price of the purchase is:', soft1)
if soft >= 100:
    soft2: float = soft1 * 0.40
    soft3 = soft1 - soft2
    print('Your discount of the purchase is:', soft3)
    disc = soft1 - soft3
    print('Discount price is:', disc)
else:
    if soft >= 50:
        soft4: float = soft1 * 0.30
        soft5 = soft1 - soft4
        print('Your discount of the purchase is:', soft5)
        disc1 = soft1 - soft4
        print('Discount price is:', disc1)
    else:
        if soft >= 20:
            soft6: float = soft1 * 0.20
            soft7 = soft1 - soft6
            print('Your discount of the purchase is:', soft7)
            disc2 = soft1 - soft7
            print('Discount price is:', disc2)
        else:
            soft8: float = soft1 * 0.10
            soft9 = soft1 - soft8
            print('Your discount of the purchase is:', soft9)
            disc3 = soft1 - soft9
            print('Discount price is:', disc3)


