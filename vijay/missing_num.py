def missing_num(lst):
    global diff
    sorted_list = sorted(lst)
    difference = sorted_list[1] - sorted_list[0]
    difference2 = sorted_list[2] - sorted_list[1]
    if difference == difference2:
        diff = difference
    else:
        difference3 = sorted_list[3]- sorted_list[2]
        if difference3 == difference2:
            diff = difference3

    min_val,max_val = sorted_list[0], sorted_list[-1]
    full_series = set(range(min_val,max_val,diff))
    missing_numbers = full_series-set(sorted_list)
    return list(missing_numbers)

a = [2,4,6,10]
print(missing_num(a))