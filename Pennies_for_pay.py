# This program is going to calculate the total salary in the given days

# Declaring the constants
total = 0.0

# Ask the user to enter the no of working days
days = int(input('Enter the number of days worked: '))

# Printing the table
print('days \t\t\t\t salary')
print('__________________________')

# Loop to calculating the total number of amount
for x in range(1, days + 1):
    y = x ** 2
    z = y / 100
    total = total + z
    print(x, '\t\t\t\t\t', z)
print()
print('The total payed at the end of the period', days, 'days is :', format(total, ',.2f'))
