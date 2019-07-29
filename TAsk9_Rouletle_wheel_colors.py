# Program to decides the colour of the roulette wheel colour
# Ask the user to select the packet between 0 to 36
packet = int(input('Enter the packet to tell the colour of that packet: '))
if packet < 0 or packet > 36:
    print('Please enter the number between 0 to 36')
else:
    if packet == 0:
        print('Your selected packet GREEN')
    elif packet < 11:
        if packet % 2 == 0:
            print('Your selected packet BLACK')
        else:
            print('Your selected packet RED')
    elif packet < 19:
        if packet % 2 == 0:
            print('Your selected packet RED')
        else:
            print('Your selected packet BLACK')
    elif packet < 29:
        if packet % 2 == 0:
            print('Your selected packet BLACK')
        else:
            print('Your selected packet RED')
    else:
        if packet % 2 == 0:
            print('Your selected packet RED')
        else:
            print('Your selected packet BLACK')

