# Program to calculate the body weight index (over weight or under weight)
# Ask the user to enter the weight and height
wt = float(input('Enter the weight in pounds: '))
ht = float(input('Enter the height in inches: '))
bml = (wt * 703) / ht ** 2
if bml < 18.5:
    print('Your total bml is less than 18.5 so your are in under weight', format(bml, '.2f'))
elif bml > 25:
    print('Your total bml is more than 25 so your are in over weight', format(bml, '.2f'))
else:
    print('Your weight is optimal', format(bml, '.2f'))
