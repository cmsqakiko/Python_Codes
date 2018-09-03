print('''Hi Joshua! Let's play a game!
Get a friend of yours and choose one of you to give me a word.
Do not tell the other person the word :) It will be between us.
Try to guess it! Goodluck!''''')
life = 3
word = input('Give me a word to store: ')
print('Thank you!!')
print('\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n   Sorry for that: ) Lets start')
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
