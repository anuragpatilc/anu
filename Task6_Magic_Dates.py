# Program to determine whether the enter date is magic date or not
# Ask the user to enter the date month and last two digit of the year
date = int(input('Enter the date: '))
month = int(input('Enter the month: '))
year = int(input('Enter last two digit of the year: '))
magic = date * month
if month <= 12:
    if year == magic:
        print('Date is magic!:', date, '/', month, '/', year, '.')
    else:
        print('Date is not magic!:', date, '/', month, '/', year, '.')
else:
    print('You entered invalid month!')
