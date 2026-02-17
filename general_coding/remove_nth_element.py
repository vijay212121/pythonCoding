def rem_n_elemnt(lst,n1):
    lst.pop(-n1)
    return lst

_lst = [1,2,3,4,5,6]
n = 2
print(rem_n_elemnt(_lst,n))