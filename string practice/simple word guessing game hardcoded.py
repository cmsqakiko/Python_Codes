print('''Hi Joshua! Let's play a game!
I have a word programmed in me.
Try to guess it! Goodluck!''''')
life = 3
word = 'montblanc'
guess = ''
while guess != word:
    guess = input('Type your Guess Word: ')
    if guess != word:
        print("I am sorry kupo! it is not the word in my mind")
        life -= 1
        if life <= 0:
            print('Game Over Kupo!')
            break
    else:
        print('Congratulations kupo! That is the word im thinking of!')
        break
print('I enjoyed playing with you kupo! thank you!')
