_list = [4, 6, 8, 3, 2, 5]
list_ = list(set(_list))
sorted_ = sorted(list_, reverse=True)
max_value = sorted_[0]
min_value = sorted_[-1]
print(f"maximum is {max_value} - minimum is {min_value}")


# def find_max_min(lst):
#     return max(lst), min(lst)
#
#
# _list = [1, 3, 5, 7, 9]
# find_max_min(_list)
