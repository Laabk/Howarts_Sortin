newlist = [12, 2, 4, 7, 24]
# swapping the 1st and last numbers

def swap_list(newlist):
    size = len(newlist)
    temp = newlist[1]
    newlist[1] = newlist[size - 1]
    newlist[size - 1] = temp
    return newlist
print(swap_list(newlist))

list = [12, 2, 4, 7, 24]
def swap_position(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
pos1, pos2 = 1, 3
print(swap_position(list, pos1-1, pos2-1))



