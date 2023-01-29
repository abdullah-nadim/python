def binary(lst,findindex):
    low = 0
    high = len(lst)
    while low<= high:
        mid = (low + high)//2
        if lst[mid] < findindex:
            low = mid
        elif lst[mid]> findindex:
            high= mid
        else:
            return mid

nums= [ 1,2,3,4,5,6,7,4,3,2,2,23,4,3,3,2,23,55]
index = binary(nums,3)
print(index)