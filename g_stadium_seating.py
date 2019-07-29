def main():
    A = 1
    B = 2
    C = 3
    Q = 4
    chose = 0
    while chose != Q:
        anu()
        chose = int(input('Enter the chose: '))
        if chose == A:
            how_many = int(input('How many ticket u want:'))
            print('The total payment', how_many, 'ticket cost', class_a(how_many))
            break
        elif chose == B:
            how_many = int(input('How many ticket u want:'))
            print('The total payment', how_many, 'ticket cost', class_b(how_many))
            break
        elif chose == C:
            how_many = int(input('How many ticket u want:'))
            print('The total payment', how_many, 'ticket cost', class_c(how_many))
            break
        elif chose == Q:
            print('Tankyou visit again')
            break
        else:
            print('Invalid!!!!!')
            break


def class_a(a):
    aa = a * 20
    return aa


def class_b(a):
    bb = a * 15
    return bb


def class_c(a):
    cc = a * 10
    return cc


def anu():
    print('      MENU      ')
    print('1) Class A sets ')
    print('2) Class B sets ')
    print('3) Class C sets ')
    print('4) Quit         ')


main()
