def selectionsort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1,len(lst)):
            if lst[min_index]> lst[j]:
                min_index=j

        lst[min_index] , lst[j]= lst[j],lst[min_index]
    return lst

nums= [43,53,23,44,98,50]
ss= selectionsort(nums)
print(ss)


def sss(arr):
    arr.sort()
    return arr
rrr= [23,54,23,54,34,80]
eee= sss(rrr)
print(eee)