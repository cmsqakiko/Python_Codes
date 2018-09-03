def kaprikar(num):
    fin = 0
    while fin != 6174:
        if len(num) <= 3:
            num = '0'+num
        fun = [num[0], num[1], num[2], num[3]]
        fun.sort()
        lo = int(''.join(fun))
        hi = int(''.join(fun[::-1]))
        print(hi,end = ' - ')
        print(lo, end = ' = ')
        fin = hi - lo
        if fin == 0:
            return 'Error'
        print(fin)
        num = str(fin)
    return fin


ast =input("Enter the number: ")

        
print(kaprikar(ast))


        


