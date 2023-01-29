def bubblesort(list):
    n=len(list)
    for a in range(n):
        for x in range(n-1):
            if list[x]> list[x+1]:
                list[x],list[x+1] = list[x+1], list[x]
    return list

nums= [ 64,33,56,76,34,90]
print(bubblesort(nums))

