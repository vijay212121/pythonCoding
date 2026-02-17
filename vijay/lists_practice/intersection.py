def inter_sect(l1, l2):
    return list(set(l1) & (set(l2)))


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(inter_sect(list1, list2))
