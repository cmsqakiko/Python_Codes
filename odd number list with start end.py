#odd number viewer
counter = 0
while True:
    try:
        if counter ==0:
            x = int(input("Enter your starting range: "))
            counter = 1
        y = int(input("Enter your ending range: "))
        if x >= y:
            print('ending range value should be greater than the starting value!')
            continue
    except:
        print('Invalid input')
        continue
    else:
        break
morty =  [i for i in range(x,y+1) if not i%2==0]
for i in range(len(morty)):
    print(morty[i], end=', ')
