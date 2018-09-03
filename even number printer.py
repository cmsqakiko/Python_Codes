def even(x):
    x += 1
    for i in range(x):
        if  (i % 2 == 0):
            print(i, end=" ")


print('''even number printer,
Define your own''')
x = int(input("enter your number here: "))
even(x)
