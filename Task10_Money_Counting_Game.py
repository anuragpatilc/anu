# Money Counting Game
# Information or manual of the game foll this to win all tha best
# 100 pennies = 1 dolor
# 20 nickels =  1 dolor
# 10 dimes = 1 dolor
# 4 quarter = 1 dolor
pennies = int(input('Enter the PENNIES: '))
nickels = int(input('Enter the NICkELS: '))
dims = int(input('Enter the DIMS: '))
quarter = int(input('Enter the QUARTER: '))

nickels1 = nickels * 5
dims1 = dims * 10
quarter1 = quarter * 25

total = pennies + nickels1 + dims1 + quarter1

win = 100 - total
if total > 100:
    print('Your entering more than one dolor')
elif win == 0:
        print('Congratulation You win the game')
else:
    print('Your entering less than one dolor')
# 25,2,4,1
