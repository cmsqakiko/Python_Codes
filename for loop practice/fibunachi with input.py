print('hiya Joshua! I am going to show you the fibunacci sequence\n it is a series where the previous number is added to the next number in the sequence')
print('i will ask for a number, this number will correspond to the\n number of numbers in the sequence i will print to the screen')

show = int(input('So Joshua, how many will I show?: '))
print( show +'? well, OK, got it, kupo!')
x = 0
y = 1
z = 0
while show >= 0:
    if x == 0 and y == 1:
        print(x)
        show -=1
        print(y)
        show -=1
    z = x + y
    print(z)
    x = y
    y = z
    show -= 1
        
print('There you have it, kupo!')
