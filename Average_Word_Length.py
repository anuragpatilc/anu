# program to add the number of strings

# constants declaration
total = str( )
total1 = 0
key = ' '

# Ask the user to enter the strings, add and average the strings
while key == ' ':
    x = str(input('enter the words: '))
    print('Space then enter to type next string')
    total = total + x
    total1 = total1 + 1
    key = input()

# Display the results
print('total string u entered:', total)
y = len(total)
print('Total length od the string:', len(total))
z = y / total1
print('Average length of the string u typed:', int(z))
