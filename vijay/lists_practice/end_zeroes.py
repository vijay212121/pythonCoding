'''
def zeroes_sort_end(lst):
    even_list = []
    odd_list = []
    zero_list = []
    for i in lst:
        if i == 0:
            zero_list.append(i)
        elif i%2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return  zero_list+even_list+odd_list


lst_ = [1,2,0,4,0,3,5,0,7]
final_list = []
print(zeroes_sort_end(lst_))
'''

lst=[1,0,2,4,0,5,0,9,0,7,0,6]
k=0
for i in range(len(lst)):
    if lst[i]!=0:
        lst[k]=lst[i]
        k+=1

for i in range(k,len(lst)):
    lst[i]=0

print(lst)





