def combine(elem, inputList):
    lst = []
    for i in range(len(inputList)+1):
        newList = inputList.copy()
        newList.insert(i, elem)
        lst.append(newList)

    return lst

def combineLists(elem, listoflists):
    lst = []
    for l in listoflists:
        tempList = combine(elem, l)
        for t in tempList:
            lst.append(t)
    return lst

def permute(lst):
    if len(lst) <= 1:
        return [lst]
    
    elem = lst[0]
    return combineLists(elem, permute(lst[1:]))


print(permute([1,2,3,4,5]))