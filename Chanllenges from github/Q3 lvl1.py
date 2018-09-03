#github python challenge
#With a given integral number n, write a program to generate
#   a dictionary that contains (i, i*i) such that is an integral number between
#       1 and n (both included). and then the program should print the dictionary.

def lim(n):
    ret = {}
    for i in range(1,n+1):
        ret[i] = i*i
    return ret

n = int(input("Enter the limit(1-n): "))
print(lim(n))
 
