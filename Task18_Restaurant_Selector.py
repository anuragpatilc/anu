# You have a group of friends coming to visit for your high school reunion, and you want to take them out to eat at a
# local restaurant.
# program that asks whether any members of your party are vegetarian, vegan, or gluten-free, to which then displays
# only the restaurants to which you may take the group.
a = input('Is anyone in your party a vegetarian?: ')
b = input('Is anyone in your party a vegan?: ')
c = input('Is anyone in your party gluten-free?: ')
print('Here are your restaurant choices:')
if a == 'no' and b == 'no' and c == 'no':
    print('Joe’s Gourmet Burgers')
if a == 'yes' and b == 'no' and c == 'yes':
    print('Main Street Pizza Company')
if a == 'yes' and b == 'yes' and c == 'yes':
    print('Corner Café')
if a == 'yes' and b == 'no' and c == 'no':
    print('Mama’s Fine Italian')
if a == 'yes' and b == 'yes' and c == 'yes':
    print('The Chef’s Kitchen')
