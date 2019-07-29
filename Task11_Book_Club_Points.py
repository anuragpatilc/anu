# Program to determined the book club points
# Ask the user to enter the how many books took in ths month
books = int(input('Enter the books you purchased in ths month: '))
if books >= 8:
    print('You earned SIXTY points')
else:
    if books >= 6:
        print('You earned FIVE points')
    else:
        if books >= 4:
            print('You earned FIFTEEN points')
        else:
            if books >= 2:
                print('You earned THIRTY points')
            else:
                print('You earned ZERO points')
