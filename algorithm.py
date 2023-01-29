"""function binary_search(list,find_value):
low= 0
high = length of the list
while low <= high:
mid = average of high and low
if mud < find_value
element will be on right side
low= mid
elif mid> find_value
element will be on the left side
high = mid
else you got the element
return element"""

def binary_search(list,find_value ):
    low = 0
    high = len(list)
    while low <= high :
        mid = (low+high)//2
        if list[mid] < find_value:
            low = mid
            print(True,1)
        elif list[mid]>find_value:
            high= mid
            print(True,2)
        else:
            print(True,3)
            return mid

list = [12,45,67,34,23]
find = 45
ind=binary_search(list,find)
print(ind)





lst = [ 2,3,4,5,6,9]
print(lst.index(9))

