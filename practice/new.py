#Find in string repeat character and its count?
from collections import Counter


def rep_char(lst):
    return Counter(lst)

_lst = "abbnsanaa"
final_list =[(k,v) for k,v in rep_char(_lst).items() if v>1]
print(final_list)