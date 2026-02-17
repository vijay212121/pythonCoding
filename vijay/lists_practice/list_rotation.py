def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]


_list = [1, 2, 3, 4, 5]
print(rotate_list(_list, 3))
