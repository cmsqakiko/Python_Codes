#palindrome
def pal(word):
    word = word.lower()
    if word.isspace() == True: return('Error: Character is all whitespace')
    word = ''.join(word.split())
    if word == word[::-1]: return 'Palindrome'
    else: return 'Not Palindrome'

word = input("Please Enter a word: ")
print(pal(word))

