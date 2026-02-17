#
# input_ = [11,62, 63,84,55]
# sorted_list = sorted(input_, reverse=True)
# for num in sorted_list:
#     print(f"{num} - {input_.index(num)}")

input_ = [11, 62, 63, 84, 55]
sorted_list = sorted(input_, reverse=True)
list_comp = [(num, input_.index(num)) for num in sorted_list]
print(list_comp)
