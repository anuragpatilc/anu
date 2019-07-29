# This program to used to calculate and convert the miles to kilometers
print('miles \t\t\t kilometers')
print('__________________________')
for x in range(10, 80 + 1, 10):
    y = x * 1.60934
    print(x, '\t\t\t\t\t', format(y, ',.2f'))
