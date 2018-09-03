
def insertion_sort(ar):
    for i in range(1,len(ar)):
        for y in range(i):
            if int(ar[i]) < int(ar[y]):
                ar[i], ar[y] = ar[y], ar[i]
                print(ar)
    return ar

ar = input('Enter the element of list separated by space: ')
ar = ar.split()
print(insertion_sort(ar))
