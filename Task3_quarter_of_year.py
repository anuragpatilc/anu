# The program is decides the quarter of the month
# Take the month
month = int(input('enter the month to know the quarter: '))
if month == 1 or month == 2 or month == 3:
    print('The enter month is in first quarter')
elif month == 4 or month == 5:
    print('The enter month is in second quarter')
elif month == 7 or month == 8 or month == 9:
    print('The enter month is third quarter')
elif month == 10 or month == 11 or month == 12:
    print('The enter month is in forth quarter')
else:
    print('ERROR!')
