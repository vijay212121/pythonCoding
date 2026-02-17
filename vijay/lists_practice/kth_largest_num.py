def largest_num(_list, _index):
    sorted_list = sorted(_list)
    result = [[num, _list.index(num)] for num in sorted_list]
    return result[_index]


lst = [12, 5, 7, 19, 3, 8, 2]
k = 3
print(largest_num(lst, k))


