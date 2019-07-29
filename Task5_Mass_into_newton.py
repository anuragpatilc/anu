# Program to convert mass to newton and decide the type of weight
# Ask the user to enter the weight in kilograms
kg = float(input('Enter the weight in kg: '))
newton = kg * 9.81
print('kg:', kg, 'newton:', format(newton, ',.2f'))
if newton >= 500:
    print('Its is too heavy', format(newton, '.2f'))
if newton <= 100:
    print('Its is too light', format(newton, '.2f'))
else:
    print('Its normal weight')
