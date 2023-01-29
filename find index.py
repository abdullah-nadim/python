def get_index(lst,find):
    index = 0
    for x in lst:
        if x== find:
            return index
        index += 1


l= [23,45,65,43]
fnd= 43
ind =get_index(l,fnd)

print(ind.__index__())