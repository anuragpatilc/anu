# Program to calculate the area of two rectangles and compare which one is grater area
# Take the length and width of the first rectangular
length1 = float(input('Enter the length of the rectangular: '))
width1 = float(input('Enter the width of the rectangular: '))
# Take the length and width of the second rectangular
length2 = float(input('Enter the length of the rectangular: '))
width2 = float(input('Enter the width of the rectangular: '))
rect1 = length1 * width1
print('The area of the first rectangular is:', rect1)
rect2 = length2 * width2
print('The area of the second rectangular is:', rect2)
if rect1 > rect2:
    print('The first rectangular area is grater than second rectangular', rect1)
elif rect1 < rect2:
    print('The second rectangular area is grater than first rectangular', rect2)
else:
    print('The area of the both rectangular are equal:', rect1, rect2)
