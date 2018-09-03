#plural generator
def plural(word):
    lstw = word[len(word)-2:len(word)]
    if word.endswith('y'):
        return word[:len(word)-1] + 'ies'
    elif lstw == 'sh' or lstw == 'ch' or lstw[1] == 's' or lstw[1] == 'x'  or lstw[1] == 'i' or lstw[1] == 'o' or lstw[1] == 'u':
        return word + 'es'
    else:
        return word + 's'

word = input('waht is the word?: ')
print(plural(word))
