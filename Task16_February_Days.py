# Program to know the days of the february
# Ask the user to enter the year to the days of the february
year = int(input('Enter the year to know the days of the february: '))
if (year % 4) == 0:
    print('This year', year, 'Have a 29 days')
else:
    if (year % 100) == 0:
        print('This year', year, 'Have a 29 days')
    else:
        if (year % 400) == 0:
            print('This year', year, 'Have a 29 days')
        else:
            print('This year', year, 'Have a 28 days')
