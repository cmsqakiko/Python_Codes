
def selection_sort(ar):
    for k in range(len(ar)):
        mini = k
        for j in range(k+1,len(ar)):
            if ar[mini] > ar[j]:
                mini = j
        ar[k], ar[mini] = ar[mini], ar[k]
        print(ar)
    return ar


ar = input('Enter the values of the list, use space as separator: ')
ar = ar.split()
print(selection_sort(ar))
