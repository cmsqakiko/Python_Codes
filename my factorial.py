def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)

print('Factorial Calculator')
joshua = int(input('What is the number?: '))
print(factorial(joshua))
