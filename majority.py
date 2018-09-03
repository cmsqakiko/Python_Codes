#majority list generator

#function below
def majority(arr):
    cont = {}
    for i in range(len(arr)):
        if not arr[i] in cont:
            cont[arr[i]] = arr.count(arr[i])
    tsk = list(cont.values())
    val = max(tsk)
    if tsk.count(val) > 1:
        return 0
    for i in range(len(arr)):
        x = cont[arr[i]]
        if x == val:
            x = arr[i]
            break
    return x
    
            
    
lst = (input('Enter the items of the list: '))
print(majority(lst.rsplit()))

