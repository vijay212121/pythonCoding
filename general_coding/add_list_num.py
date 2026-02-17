def add_list_num(_dict):
    result = []
    for key,value in _dict.items():
        result.append(key+value)
    return result


lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9,10]
print(add_list_num(dict(zip(lst1,lst2))))
