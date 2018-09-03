def bt(b):
    bn = []
    while True:
        if b == 1:
            bn.append(1)
            break
        else:
            bn.append(b %2)
            b = b //2
    bn = ''.join(str(i) for i in bn)
    return bn.count('1')

b = int(input('Enter a decimal integer to be converted: '))
print(bt(b))
