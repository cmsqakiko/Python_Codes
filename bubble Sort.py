
def bubble_sort(ar):
    count = 0
    for i in range(len(ar)-1,0,-1):
        for x in range(i):
            if int(ar[x]) > int(ar[x+1]):
                ar[x], ar[x+1] = ar[x+1], ar[x]
            print(ar)
            count +=1
    print(count)
    return ar

ar = input("Enter the list of numbers to be sorted: ")
ar = ar.split()
print(bubble_sort(ar))
