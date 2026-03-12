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

# Move all zeros in a list to the end while maintaining the order of non-zero elements

lst = [1, 0, 2, 4, 0, 5, 0, 9, 0, 7, 0, 6]
k = 0  # Pointer to place the next non-zero element

# Step 1: Move all non-zero elements to the front
for i in range(len(lst)):
    if lst[i] != 0:      # Check if current element is non-zero
        lst[k] = lst[i]  # Place it at index k
        k += 1           # Move k to the next position

# Step 2: Fill the remaining positions with zeros
for i in range(k, len(lst)):
    lst[i] = 0

# Result
print(lst)





