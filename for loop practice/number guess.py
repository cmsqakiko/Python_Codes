
print('Montblanc Here! Let us play another game \n guess the number programmed to me')

number = int(input('Give me a number, kupo!  '))
guess = 0
while True:
    guess = int(input("What is your guess? : "))
    if guess < number:
        print('My number is bigger kupo!')
    elif guess > number:
        print('My number is smaller kupo!')
    else:
        print("That is the number, kupo!")
        break
