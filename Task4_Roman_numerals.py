#  Roman Numerals
# Write a program that prompts the user to enter a number within the range of 1 through 10.
# The program should display the Roman numeral version of that number. If the number is
# outside the range of 1 through 10, the program should display an error message.


# Program to teach the 1 to 10 roman numerical
# Take the corresponding  numerical number to get the roman number (1 to 10)
num = int(input('Enter the number (1 to 10) to get a corresponding roman number: '))
if num == 1:
    print('1 = I')
elif num == 2:
    print('2 = II')
elif num == 3:
    print('3 = III')
elif num == 4:
    print('4 = VI')
elif num == 5:
    print('5 = V')
elif num == 6:
    print('6 = VI')
elif num == 7:
    print('7 = VII')
elif num == 8:
    print('8 = VIII')
elif num == 9:
    print('9 == IX')
elif num == 10:
    print('10 = X')
else:
    print('ERROR')
