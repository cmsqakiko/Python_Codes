#create a function that will print the majority character in a function of any lenght
maj = [1,2,3,2,3,4,5,7,8,2]

printer =0
def function(maj):
    for i in range(len(maj)):
        #test function
        printer = maj.count(maj[i])
        print('the character ' + str(maj[i]) + ' occurs:')
        print(str(printer) + 'time/s')
function(maj)
